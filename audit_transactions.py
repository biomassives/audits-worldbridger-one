import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from datetime import datetime

class TinyBoxesAnalyzer:
   def __init__(self, subgraph_url, batch_size=1000):
       self.url = subgraph_url
       self.batch_size = batch_size
       os.makedirs('data', exist_ok=True)

   def query_subgraph(self, query):
       try:
           headers = {
               'Content-Type': 'application/json',
               'Authorization': 'Bearer 473e06973b89df6baa6542e9d95a96f9'
           }
           response = requests.post(self.url, headers=headers, json={'query': query})
           return response.json().get('data', {})
       except Exception as e:
           print(f"Error: {e}")
           return {}

   def get_all_tokens(self, skip=0):
       query = f"""
       {{
           tokens(first: {self.batch_size}, skip: {skip}) {{
               id
               tokenId
               owner
               animation
               shapes
               hatching
               size
               spacing
               mirroring
               color
               contrast
               shades
               scheme
               type
               columns
               hue
               lightness
               saturation
               spread
               minted
               phase
           }}
       }}
       """
       return self.query_subgraph(query).get('tokens', [])

   def get_all_tokens_paginated(self, total=5622):
       all_tokens = []
       for skip in range(0, total, self.batch_size):
           print(f"Fetching tokens {skip} to {min(skip + self.batch_size, total)}")
           tokens = self.get_all_tokens(skip)
           all_tokens.extend(tokens)
           if not tokens:
               break
       return all_tokens

   def analyze(self):
       timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
       
       # Fetch and process tokens in batches
       all_tokens = self.get_all_tokens_paginated()
       tokens_df = pd.DataFrame(all_tokens)
       
       # Save raw data
       tokens_df.to_json(f'data/raw_tokens_{timestamp}.json')
       
       # Basic analysis
       analysis = {
           'timestamp': timestamp,
           'total_tokens': len(tokens_df),
           'unique_owners': len(tokens_df['owner'].unique()) if not tokens_df.empty else 0,
           'trait_distributions': {},
       }

       # Analyze distributions
       numeric_columns = ['shapes', 'hatching', 'contrast', 'shades', 'scheme', 'hue', 'saturation']
       for col in numeric_columns:
           if col in tokens_df.columns:
               analysis['trait_distributions'][col] = tokens_df[col].value_counts().to_dict()

       # Save analysis results
       with open(f'data/analysis_{timestamp}.json', 'w') as f:
           json.dump(analysis, f)

       # Generate visualizations
       self.generate_visualizations(tokens_df, timestamp)
       
       return analysis

   def generate_visualizations(self, tokens_df, timestamp):
       # Trait distributions
       if not tokens_df.empty:
           plt.figure(figsize=(20, 15))
           plot_cols = ['shapes', 'hatching', 'contrast', 'shades', 'hue', 'saturation']
           for i, col in enumerate(plot_cols):
               if col in tokens_df.columns:
                   plt.subplot(3, 2, i+1)
                   sns.histplot(data=tokens_df, x=col)
                   plt.title(f'{col.title()} Distribution')
           plt.tight_layout()
           plt.savefig(f'data/trait_distributions_{timestamp}.png')
           plt.close()

           # Owner distribution
           plt.figure(figsize=(15, 8))
           owner_counts = tokens_df['owner'].value_counts()
           sns.barplot(x=range(len(owner_counts[:50])), y=owner_counts[:50])
           plt.title('Top 50 Owners by Token Count')
           plt.xlabel('Owner Rank')
           plt.ylabel('Number of Tokens')
           plt.xticks(rotation=45)
           plt.tight_layout()
           plt.savefig(f'data/ownership_distribution_{timestamp}.png')
           plt.close()

if __name__ == "__main__":
   analyzer = TinyBoxesAnalyzer('https://api.studio.thegraph.com/query/97143/tinyboxes/0.3.3')
   analysis = analyzer.analyze()
   print(f"Analysis complete!")
   print(f"Total Tokens: {analysis['total_tokens']}")
   print(f"Unique Owners: {analysis['unique_owners']}")
   print(f"Data saved in ./data directory")
