# O-dang!
The Ontology of Dangerous Speech Messages (O-Dang!) is a systematic and interoperable Knowledge Graph (KG) for the collection of linguistic annotated data. 
O-Dang! is designed to gather and organize Italian datasets into a structured KG, according to the principles shared within the Linguistic Linked Open Data community. The ontology has also been designed to account a <a href="https://pdai.info/">perspectivist</a> approach, since it provides a model for encoding both gold standard and single-annotator labels in the KG.
## SPARQL QUERIES

### STATISTICS ABOUT CORPORA
<a href="https://kgccc.di.unito.it/sparql/o-dang?default-graph-uri=&query=PREFIX+%3A+%3Chttp%3A%2F%2Fhatespeech.di.unito.it%2Fodang%23%3E%0D%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+dul%3A+%3Chttp%3A%2F%2Fwww.ontologydesignpatterns.org%2Font%2Fdul%2FDUL.owl%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+dcterm%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0D%0APREFIX+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0APREFIX+dct%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0D%0A%0D%0ASELECT+DISTINCT+*+%0D%0AWHERE+%7B%0D%0A++%3Ftweet+a+%3ATweet%3B%0D%0A+++++dcterm%3Adescription+%3Ftext%3B%0D%0A+++++%3AisPartOf+%3Fdataset+.%0D%0A%3Fdataset+rdfs%3Alabel+%3Fd_label%7D+LIMIT+100%0D%0A%0D%0A++%0D%0A%0D%0A&format=text%2Fhtml&timeout=0&signal_void=on">Select all the tweets and their data sets </a>

<a href="https://kgccc.di.unito.it/sparql/o-dang?default-graph-uri=&query=PREFIX+%3A+%3Chttp%3A%2F%2Fhatespeech.di.unito.it%2Fodang%23%3E%0D%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+dul%3A+%3Chttp%3A%2F%2Fwww.ontologydesignpatterns.org%2Font%2Fdul%2FDUL.owl%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+dcterm%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0D%0APREFIX+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0APREFIX+dct%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0D%0A%0D%0ASELECT+%28sample%28%3Fd_label%29+as+%3Fdataset_label%29+%28count%28%3Fdataset%29+as+%3Foccurrences%29+%0D%0AWHERE+%7B%0D%0A++%3Ftweet+a+%3ATweet%3B%0D%0A+++++dcterm%3Adescription+%3Ftext%3B%0D%0A+++++%3AisPartOf+%3Fdataset+.%0D%0A%3Fdataset+rdfs%3Alabel+%3Fd_label%7D+GROUP+BY+%3Fdataset%0D%0A%0D%0A++%0D%0A%0D%0A&format=text%2Fhtml&timeout=0&signal_void=on"> Count all tweets within each data set </a>
    
### COMMUNICATIVE SITUATIONS
<a href="https://kgccc.di.unito.it/sparql/o-dang?default-graph-uri=&query=PREFIX+%3A%3Chttp%3A%2F%2Fhatespeech.di.unito.it%2Fodang%23%3E%0D%0Aselect+distinct+%3Fadj+%3Fuser+%3Fmessage+%3Frole+where+%7B%0D%0A%3Fadj+a+%3AAdjacencyPair%3B+%3AisSettingFor+%3Fuser%2C%3Fmessage+.%0D%0A%3Fuser+a+%3APerson.%0D%0A%3Fmessage+a+%3ATweet%3B+%3AwasAssociatedWith+%3Fperson.%0D%0A%3Fmessage+%3AhasRole+%3Fr+.%0D%0A%3Fr+a+%3Frole%0D%0A%7D+order+by+%3Fadj&format=text%2Fhtml&timeout=0&signal_void=on">Find all the communicative situations </a>

### ANNOTATIONS
<a href="https://kgccc.di.unito.it/sparql/o-dang?default-graph-uri=https%3A%2F%2Fkgccc.di.unito.it%2Fo-dang&query=PREFIX+%3A+%3Chttp%3A%2F%2Fhatespeech.di.unito.it%2Fodang%23%3E%0D%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+dul%3A+%3Chttp%3A%2F%2Fwww.ontologydesignpatterns.org%2Font%2Fdul%2FDUL.owl%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+dcterm%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0D%0APREFIX+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0APREFIX+dct%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0D%0A%0D%0ASELECT+distinct+%3Ftweet+%3Fphenomenon+%3Fvalue+%3Fannotator%0D%0AWHERE+%7B%0D%0A++%3Ftweet+a+%3ATweet%3B%0D%0A+++++%3AisDescribedBy+%3Fdesc+%3B+%3AwasAssociatedWith+%3Fannotator+.%0D%0A%3Fdesc+%3Avalue+%3Fv+.%0D%0A%3Fv+%3AhasValue+%3Fvalue+.%0D%0A%3Fdesc+a+%3Fphenomenon+.%0D%0A%3Fdesc+%3AwasAssociatedWith+%3Fannotator+.%0D%0A%3Fv+%3AwasAssociatedWith+%3Fannotator+.%0D%0A%0D%0A%7D+order+by+%3Ftweet+limit+1000%0D%0A%0D%0A++%0D%0A%0D%0A&format=text%2Fhtml&timeout=0&signal_void=on"> Find all the Twitter posts annotated with unaggregated labels </a>
      
