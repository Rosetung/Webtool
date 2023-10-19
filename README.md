# Webtool

# GMS6907 Project Webtool - Ez Flow Plots 
URL: https://ezflow.streamlit.app/

A python based webtool that allows users to design flow cytometery panels and subsequent data analysis and visualisation of flow data efficiently.

## Goals for the webtool Ez Flow Plots
**Main goal**: To be able to plot bar graphs (with individual values) for any data in excel or csv format, with appropriate statistical tests. 

## Specific goals
1. We should be able to upload/input files - in excel format or csv format. 
2. Define group by condition -> select categorical varibale for analysis (refer to iris dataset)
3. Indicate number of count for each condition/group 
4. Select parameters to plot for bar graph - must also show individual datapoints, mean, standard error
5. Output a table with mean and standard error for the corresponding parameter
6. Select the statistical analysis to do for the groups selected above
7. Output a table with multiple comparisons, with significance
8. Ideally, output bargraphs with statistics 

# User guide for **Ez Flow Plots**
## What is Ez Flow Plots?

Ez Flow Plots is an online free webtool that serves to help users in both the planning and analysis of flow cytometry experiments. The first page of the webtool is designed to be used during the planning stage of experiments and provides users with appropriate combinations of fluorophores for their chosen cellular markers. The second page allows data visualisation and statistical analysis for multiple parameters at once, generating graphs and statistical calculations efficiently.


## Use cases:
**Ez Flow Plots has two main functions - Flow panel design and Data visualisation and analysis.**
### Flow panel design:
- Design panel for any cytometer configuration. Default configuration is for Duke-NUS BD Fortessa Analyzer with 5 lasers
- In case you have many markers and various sets of fluorochromes for each marker and would like to design a panel without having to check excitation/emission spectrum manually.
### Data analysis and visualisation:
- This tool was created particularly for flow data exported as tables from flowjo, with multiple parameters. You can now easily get all your bar graphs, do your correlation analysis and inferential statistics in minutes!
- Any dataset with a combination of numerical and at least one categorical variable, prepared in excel or csv format, can be visualised as charts and analysed with different statistical tests.


## How to use the webtool?


### To run the webtool locally:
1. Technical requirements
    - Python 3.9 (or later).
    - Any text editor (e.g. Sublime or Visual Studio Code) to allow editing of Python (.py) files.
2. Install Streamlit
    - Run the following code in Terminal:
    ```
    pip install streamlit
    ```
3. Install packages 

        ```
        pip install pandas
        pip install numpy
        pip install plotly
        pip install seaborn → version 12
        pip install matplotlib 
        pip install scipy
        pip install pingouin
        ```


4. Download the folders and .py files
    - Download the ‘flow_webtool’ folder to your home directory. 
    <img width="624" alt="image" src="https://user-images.githubusercontent.com/110210542/195425631-76544c0f-8af7-45ea-b854-40379d7d1a00.png">


5. File names:
    - 👩‍💻_Design_your_flow_panel.py
    - 1_📊_Plot_your_figures.py
6. To run webtool locally
    - Type the following in Terminal:

        ```
        mkdir flow_webtool
        cd flow_webtool
        streamlit run 👩‍💻_Design_your_flow_panel.py

        ```

## Step by step guide for webtool use:
### A. Design your flow panel (before running FACS, while designing your experiment)

1. Upload the details of the FACS machine configuration in Excel file. Please see the screenshot below for the format. 
<img width="624" alt="image" src="https://user-images.githubusercontent.com/110210542/195425684-29e605d2-8551-4bff-a36e-2b9b3ece0db7.png">
**If none is uploaded, the Duke-NUS FACS machine configuration (BD LSRFortessa; 5 lasers) will be used.**

<img width="614" alt="image" src="https://user-images.githubusercontent.com/110210542/195425709-30faddf8-3a12-42f0-9b2d-05663022f58b.png">

2. Select how many markers you will be staining.
3. Enter the name of your markers and all available fluorophores.
4. An overview of your markers and their corresponding fluorophores will be displayed.
5. The final section will display all compatible flow panels (with all markers in different channels).
### B. Plot your figures (for after FACS, to visualise/plot your results)

1. Preparing your flow data:
    - Prepare Excel or CSV file of your flow data exported from FlowJo.
    - Ensure headings are labelled as you would want them to be displayed in your final figures (avoid using symbols as this will cause problems for downloading your figures)
    - If the file is exported as a table from flowjo software, it will only have sample names and not group names. Add columns and indicate groups names (categorical variables) as below:

    <img width="612" alt="Picture 4" src="https://user-images.githubusercontent.com/110210542/195425833-0da8eb0c-12b3-481a-a6ca-af97520a4ac2.png">


2. Uploading your flow data:
    - Choose the file type to upload - csv versus excel
    - Either use **Browse** option to upload file or drag and drop your file
    - Only one file can be uploaded at a time
    - If excel file is uploaded, you can choose the sheet number containing your dataset
    - Table containing your uploaded dataset will appear for you to ensure the correct dataset has been uploaded


    <img width="612" alt="Picture 5" src="https://user-images.githubusercontent.com/110210542/195425870-d1f8e4d6-4100-4deb-945e-a0fbbd60c4c9.png">


3. First tab (Plotting bar graphs)
    - Define the different groups and subgroups to be visualised in your bar graphs.
        1. At least one categorical variable needs to be defined 
        2. The tool will display the count for each group. 
    - Select the parameters you want to plot as bar graphs (all parameters will be chosen by default).
    - The tool will generate bar graphs with the mean, standard error, and individual data points for the chosen parameters.
    - Click on the ‘Download figures’ button to download all your bar graphs as EPS files.

        <img width="612" alt="Picture 6" src="https://user-images.githubusercontent.com/110210542/195425892-aabb10c0-9a05-4e10-8493-fb2d24f55144.png">   

        <img width="612" alt="Picture 7" src="https://user-images.githubusercontent.com/110210542/195425912-b231da54-6bd0-4876-b594-58956eb940e2.png">

        <img width="612" alt="Picture 8" src="https://user-images.githubusercontent.com/110210542/195425942-e4865a81-7ec7-4047-8f71-2613728c29dd.png">



4. Second tab (Correlation analysis)
    1. _Analysing correlation with scatterplot:_
        - Select two parameters to visualise their correlation as a scatter plot.
        - The webtool will calculate the Pearson correlation coefficient and Spearman’s rank correlation coefficient and display them below the scatter plot along with their corresponding p-values. 
        - Click on the ‘Download figure’ button to download an SVG file of the scatter plot.
    2. _Correlation matrix with heatmap and pairwise plots:_
        - Select any number of parameters to generate a heatmap of correlation matrix. By default, all parameters will be selected. 
        - Click on the ‘Download figure’ button to download an SVG file of the heatmap.
        - The webtool will also generate a pairwise plot of all parameters included in the heatmap. 
        - For pairwise plots, choose a categorical variable to visualise data stratified into different groups. 
        - Click on the ‘Download figure’ button to download an SVG file of the pairwise plot.

        <img width="612" alt="Picture 9" src="https://user-images.githubusercontent.com/110210542/195425970-5d808bcf-cc3c-4d7d-97ec-8ad9218a7377.png">

5. Third tab (Statistical calculations):
    1. Select the appropriate statistical test for your data:
        - One Sample Data
        - Paired Sample Data
        - Two Sample Data
        - One-way ANOVA
        - Two-way ANOVA
    2. Input the appropriate variables to perform statistical analysis. The webtool will perform a normality test (displayed as a QQ plot) and generate the p-value at the bottom of the page.

## Similar webtools:

### Flow panel design alternatives:
    1. Various companies provide online tools - ThermoFisher, Fluorofinder, Abcam
    2. Issues:
        - Need to login, register account, requires payment
        - Predefined set of markers → cannot add new ones to the list
        - Does not allow input of different fluorochromes for the same marker, and vice versa, does not allow for input of different markers with same fluorochrome. See below example:
<img width="612" alt="Picture 10" src="https://user-images.githubusercontent.com/110210542/195426016-f1e212eb-5f1f-48a9-a83a-4966485976c8.png">

### Alternative tools for plotting graphs:
    1. Graphpad:
        - EXPENSIVE (and admin staff NEVER renew licence on time 🙁) 
        - **TIME CONSUMING** to plot data for each parameter one by one. 
        - Multiple sheets need to be created for same data set depending on whether you want to compare 2 samples, column data analysis (one-way ANOVA) or grouped data analysis (two-way ANOVA)
    2. Flowjo plugins:
        - Expensive, needs dongle to use, and plugins are only flowjo data to be used within that software
        - Available plugins (ViolinBox, Correlate) - need separate plugin for each data visualisation method. 
        - No inferential statistics function.
<img width="524" alt="image" src="https://user-images.githubusercontent.com/110210542/195428821-aebb491a-c18f-4a7b-86ae-3dd4b59585d4.png">


### How is Ez Flow Plot better?
    1. Free, intuitive and easy to use
    2. Serves two purpose on the same platform
    3. Serves two purpose on the same platform - designing flow panel and data analysis and data visualisation
    - Flow panel design:
        1. Unlike other available tools, our web tool allows the user to input all your available antibodies (any marker with any number of fluorochromes). 
        2. The tool then suggests multiple panel options as long as there is at least one unique, compatible fluorochrome for each marker.
    - Data analysis and visualisation:
        1. The key advantage of our web tool is that it allows you to generate all your charts and do your various statistical analysis in a single step! Saves so much time!!!
        2. You can also do various correlation analysis and generate figures. 
        3. Before doing the statistical tests, it also checks for normality of your data so that you can decide whether to transform the data or not. 
        4. All figures are downloadable in eps or svg formats, ensuring that they are in high quality format for publication.

## Current limitations and future work:

### Component A: Designing flow panel
    1. Currently, even if one of the markers do not have an unique compatible fluorochrome then the entire panel does not appear. Nor does it say which fluorochrome/marker needs to be changed. Can update code to help identify this and fix this. 
    2. Improve code to upload an infinite number of markers to be used in cases like CyTOF panel design.
    3. Input data on antigen intensity for that cell population, such that brightest fluorochrome can be auto selected for weakest antigen.
### Component B: Plotting figures
    1. Generate statistics results as a downloadable report along with all graphs.
    2. Lack of multiple comparsions.
    3. Be able to indicate statistically significant differences between groups on bar graphs (like in GraphPad) to highlight key results. 


## Credits:

For the GMS6907 module project by Allyson, Eunji, Monica and Rose from Duke-NUS EID.

