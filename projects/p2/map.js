$("#container1").datamap({
   scope: 'world',
   geography_config: {
     borderColor: 'gray',
     highlightBorderColor: '#606060',
     popupTemplate: _.template([
       '<div class="hoverinfo">',
       '<% if (data.name) { %> <strong><%= data.name %></strong><br/><% } %>',
       '<% if (data.spending) { %>',
       'Military Spending: <%= data.spending %><br/> <% } %>',
       '</div>'
      ].join('') )
   },
   fills: {
     spending1: '#005A32',
     spending2: '#238B45',
     spending3: '#41AB5D',
     spending4: '#74C476',
     spending5: '#A1D99B',
     spending6: '#C7E9C0',
     defaultFill: '#F7F7F7' 
   },
   data: {
     'USA': {
       fillKey: 'spending1',
       name: 'United States',
       spending: 711421000000
      },
     'GBR': {
       fillKey: 'spending2',
       name: 'United Kingdom',
       spending: 39116000000
      },
     'CAN': {
       fillKey: 'spending3',
       name: 'Canada',
       spending: 24486000000
      },
     'AUS': {
       fillKey: 'spending4',
       name: 'Australia',
       spending: 25905000000
      },
     'IRQ': {
       fillKey: 'spending4',
       name: 'Iraq',
       spending: 6839000000
      },
     'POL': {
       fillKey: 'spending4',
       name: 'Poland',
       spending: 28757000000
      },
     'KOR': {
       fillKey: 'spending5',
       name: 'South Korea',
       spending: 34113000000
      },
     'UKR': {
       fillKey: 'spending5',
       name: 'Ukraine',
       spending: 32496000000
      },
     'ITA': {
       fillKey: 'spending5',
       name: 'Italy',
       spending: 24772000000
      },
     'GEO': {
       fillKey: 'spending6',
       name: 'Georgia',
       spending: 718000000
      },
     'ESP': {
       fillKey: 'spending6',
       name: 'Spain',
       spending: 10898000000
      },
     'DNK': {
       fillKey: 'spending6',
       name: 'Denmark',
       spending: 26091000000
      },
    'NLD': {
       fillKey: 'spending6',
       name: 'Netherlands',
       spending: 8459000000
      }
   }
});