$("#container1").datamap({
   scope: 'europe',
   geography_config: {
     borderColor: 'gray',
     highlightBorderColor: '#606060',
     popupTemplate: _.template([
       '<div class="hoverinfo">',
       '<% if (data.name) { %> <strong><%= data.name %></strong><br/><% } %>',
       '<% if (data.population) { %>',
       'Population: <%= data.population %><br/> <% } %>',
       '</div>'
      ].join('') )
   },
   fills: {
     pop1: '#BD0026',
     pop2: '#F03B20',
     pop3: '#FD8D3C',
     pop4: '#FEB24C',
     pop5: '#FED976',
     pop6: '#FFFFB2',
     defaultFill: '#C0C0C0' 
   },
   data: {
     'RUS': {
       fillKey: 'pop1',
       name: 'Russia',
       population: 143369806
      },
     'DEU': {
       fillKey: 'pop2',
       name: 'Germany',
       population: 81946000
      },
     'TUR': {
       fillKey: 'pop3',
       name: 'Turkey',
       population: 75627384
      },
     'FRA': {
       fillKey: 'pop4',
       name: 'France',
       population: 65605000
      },
     'GBR': {
       fillKey: 'pop4',
       name: 'United Kingdom',
       population: 63181775
      },
     'ITA': {
       fillKey: 'pop4',
       name: 'Italy',
       population: 59499534
      },
     'ESP': {
       fillKey: 'pop5',
       name: 'Spain',
       population: 47265321
      },
     'UKR': {
       fillKey: 'pop5',
       name: 'Ukraine',
       population: 45560251
      },
     'POL': {
       fillKey: 'pop5',
       name: 'Poland',
       population: 38533789
      },
     'ROU': {
       fillKey: 'pop6',
       name: 'Romania',
       population: 19043767
      },
     'NLD': {
       fillKey: 'pop6',
       name: 'Netherlands',
       population: 16778806
      },
     'BEL': {
       fillKey: 'pop6',
       name: 'Belgium',
       population: 11145453
      },
    'GRC': {
       fillKey: 'pop6',
       name: 'Greece',
       population: 10815197
      },
     'PRT': {
       fillKey: 'pop6',
       name: 'Portugal',
       population: 10562178
      },
     'CZE': {
       fillKey: 'pop6',
       name: 'Czech Republic',
       population: 10513209
      },
     'HUN': {
       fillKey: 'pop6',
       name: 'Hungary',
       population: 9957731
      },
     'SWE': {
       fillKey: 'pop6',
       name: 'Sweeden',
       population: 9561254
      },
     'BLR': {
       fillKey: 'pop6',
       name: 'Belarus',
       population: 9462400
      },
     'AUT': {
       fillKey: 'pop6',
       name: 'Austria',
       population: 8489482
      },
     'CHE': {
       fillKey: 'pop6',
       name: 'Switzerland',
       population: 8014000
      },
     'BGR': {
       fillKey: 'pop6',
       name: 'Bulgaria',
       population: 7364570
      },
     'SRB': {
       fillKey: 'pop6',
       name: 'Serbia',
       population: 7241295
      },
     'DNK': {
       fillKey: 'pop6',
       name: 'Denmark',
       population: 5602628
      },
     'SVK': {
       fillKey: 'pop6',
       name: 'Slovakia',
       population: 5445324
      },
     'FIN': {
       fillKey: 'pop6',
       name: 'Finland',
       population: 5431750
      },
     'NOR': {
       fillKey: 'pop6',
       name: 'Norway',
       population: 5051275
      },
     'IRL': {
       fillKey: 'pop6',
       name: 'Ireland',
       population: 4588252
      },
     'HRV': {
       fillKey: 'pop6',
       name: 'Croatia',
       population: 4290612
      },
     'BIH': {
       fillKey: 'pop6',
       name: 'Bosnia',
       population: 3839737
      },
     'MDA': {
       fillKey: 'pop6',
       name: 'Moldova',
       population: 3839737
      },
     'ALB': {
       fillKey: 'pop6',
       name: 'Albania',
       population: 2821977
      },
     'LTU': {
       fillKey: 'pop6',
       name: 'Lithuania',
       population: 2972949
      },
     'MKD': {
       fillKey: 'pop6',
       name: 'Macedonia',
       population: 2059794
      },
     'SVN': {
       fillKey: 'pop6',
       name: 'Slovenia',
       population: 2059299
      },
     'LVA': {
       fillKey: 'pop6',
       name: 'Latvia',
       population: 2027000
      },
     'XK': {
       fillKey: 'pop6',
       name: 'Kosovo',
       population: 4290612
      },
     'EST': {
       fillKey: 'pop6',
       name: 'Estonia',
       population: 1286540
      },
     'CYP': {
       fillKey: 'pop6',
       name: 'Cyprus',
       population: 862000
      },
     'MNE': {
       fillKey: 'pop6',
       name: 'Montenegro',
       population: 620029
      },
     'LUX': {
       fillKey: 'pop6',
       name: 'Luxembourg',
       population: 465000
      },
     'ISL': {
       fillKey: 'pop6',
       name: 'Iceland',
       population: 321857
      }
   }
});