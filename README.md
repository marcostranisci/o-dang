# o-dang
O-DANG: the Ontology of DANGerous Speech

## SPARQL QUERIES

<li>
<a href="http://212.237.50.39:8080/fuseki/dataset.html?tab=query&ds=/o-dang#query=PREFIX+%3A+%3Chttp%3A%2F%2Fhatespeech.di.unito.it%2Fodang%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+dul%3A+%3Chttp%3A%2F%2Fwww.ontologydesignpatterns.org%2Font%2Fdul%2FDUL.owl%23%3E%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+dcterm%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0APREFIX+dct%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0A%0ASELECT+*+%0AWHERE+%7B%0A++%3Ftweet+a+%3ATweet%3B%0A+++++dcterm%3Adescription+%3Ftext%3B%0A+++++%3AisPartOf+%3Fdataset+.%0A%3Fdataset+rdfs%3Alabel+%3Fd_label%7D+LIMIT+100%0A%0A++%0A%0A">Select all the tweets and their data sets </a>

  <li>
<a href="http://212.237.50.39:8080/fuseki/dataset.html?tab=query&ds=/o-dang#query=PREFIX+%3A+%3Chttp%3A%2F%2Fhatespeech.di.unito.it%2Fodang%23%3E%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+dul%3A+%3Chttp%3A%2F%2Fwww.ontologydesignpatterns.org%2Font%2Fdul%2FDUL.owl%23%3E%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+dcterm%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0APREFIX+dct%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0A%0ASELECT+(sample(%3Fd_label)+as+%3Fdataset_label)+(count(%3Fdataset)+as+%3Foccurrences)+%0AWHERE+%7B%0A++%3Ftweet+a+%3ATweet%3B%0A+++++dcterm%3Adescription+%3Ftext%3B%0A+++++%3AisPartOf+%3Fdataset+.%0A%3Fdataset+rdfs%3Alabel+%3Fd_label%7D+GROUP+BY+%3Fdataset%0A%0A++%0A%0A"> Count all tweets within each data set </a>

