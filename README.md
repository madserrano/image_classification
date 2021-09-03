# Capstone project: Product Look App

In this project, dataset was collected by scrapping product images from Canadian Tire website using python code, with Beautiful Soup and Selenium web driver as primary modules. A total of 103,500 images were collected, pre-processed, and labeled with 207 categories. CNN was leveraged in creating the multi-class classification model. Seven experimental models were built for each five sections (Automotive, Tools & Hardware, Home & Pets, Sports and Recreation and Outdoor Living). Various steps were conducted to reduce overfitting such as regularization, weight constraints and image augmentation. Streamlit, an opensource web framework was utilized to create a web application that runs the model files. The whole application including codes, configuration set-up and software dependencies were compiled into one Docker image file. Heroku and Azure were used as Development and Production environment, respectively. The existing version of the application is now running in production environment and can be accessed through this link: http://productlookapp.eastus.cloudapp.azure.com:8501/. 

For the next version, model and training set enhancement will be the primary focus. Since the models only yield 50-65% accuracy during evaluation, further training, and hyper-parameter tuning needs to be done to improve the model performance. Moreover, having an adequate and balanced dataset is crucial in implementing this project. Hence, data collection is also something that needs to be planned thoroughly for a longer timeline, to obtain suitable and sufficient dataset.


## To run in your local:
1. Clone the project.
2. Install the required libraries (streamlit, skimage, opencv, tensorflow, numpy, pandas)
3. Run streamlit in your cmd or conda using this command: streamlit run prod_recog2.py <br>
   <i>**Note: ensure that you are inside the <project>/app_codes directory when you run this command.</i>
4. Webpage will automatically open in your browser. If not, manually type this in the address box: http://localhost:8501/
5. To edit the code, open prod_recog2.py in your python IDE or Notepad++ <br>
6. Ensure that you have the 5 model files (links below) uploaded in your machine under app_codes folder.
   
Alternatively, if you have docker desktop installed in your machine, you may opt to pull the docker image instead by executing: **docker pull madserrano/prodrecog**

## H5 FILES:
1. Home and Pets: <br>
   Pruned: https://drive.google.com/file/d/1-QG3rTqyVcXjw3UQlT1QXCdR5ULlpaUF/view?usp=sharing <br>
   Zip3: https://drive.google.com/file/d/1-Y6HAGG058oCUzis5z42BfyAQfNkc3Oa/view?usp=sharing <br>
2. Sports and Recreation: <br>
   Pruned: https://drive.google.com/file/d/1-PZXJz5HT4yK0PqrWi_OmJGOhoZ3YXqZ/view?usp=sharing <br>
   Zip3: https://drive.google.com/file/d/1-RoROJtITblDnMBTYqPfY32NalAJWyLa/view?usp=sharing <br>
3. Outdoor Living <br>
   Pruned: https://drive.google.com/file/d/1-Vi4hyMC-4qZVS1qSgZZ2rKtBcuaBRDw/view?usp=sharing <br>
   Zip3: https://drive.google.com/file/d/1-VzIC5AysoL_c5eSAFMEfpZEA75M0OSz/view?usp=sharing <br>
4. Tools and Hardware <br>
   Pruned: https://drive.google.com/file/d/1-IcSU9zJJ7cgz-F4eIj_heJfUii1EH3o/view?usp=sharing <br>
   Zip3: https://drive.google.com/file/d/1-RF1SBJyGXJ-bE5pECvdX6Ja-K6T4-01/view?usp=sharing <br>
5. Automotive: <br>
   Pruned: https://drive.google.com/file/d/1-SxflAxjxrvqL55G6KUc0AqXAFuwkRNK/view?usp=sharing <br>
   Zip3: https://drive.google.com/file/d/1-TzSg6fHS7jiYs-6prLZi3vaapZXhuVB/view?usp=sharing
   
## Code Contributors:
https://github.com/madserrano (front-end, back-end)
https://github.com/jonatasaguiar (back-end)
https://github.com/iamAjayDahiya/ (front-end)
