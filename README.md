# DA2_Final_Project

### Project Overview

This is my final project for Code Louisville's Data Analysis track, ending summer 2023. I will be delving into some data sets from a competition hosted by retail fashion brand H&M last year. All relevant data can be found at a. My objective is to examine trends in customer purchasing history across age groups. A visualization of these results can be viewed on my Tableau Pubilc profile.
<div class='tableauPlaceholder' id='viz1690261203034' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fa&#47;FashionData&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FashionData&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fa&#47;FashionData&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1690261203034');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1027px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>


### Data Download

Data was downloaded in csv format from https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data, then extracted to the 'Data' folder in this repository. In order to access this data, it is necessary to have an active Kaggle account with which you must accept the rules of the competition as set forth by H&M. Note: the competition is no longer active and the rules state that the data is acceptable for use in educational purposes, which is my intent. 


### Setting Up The Virtual Environment

For Windows users: 
  - using GitBash, make sure you are in the correct folder, then enter the following commands:
    -  py -m venv venv
    -  source venv/Scripts/activate
    -  pip install -r requirements.txt
   
For Mac OS users:
  - using GitBash, make sure you are in the correct folder, then enter the following commands:
    -  py -m venv venv
    -  source venv/bin/activate
    -  pip install -r requirements.txt
    
