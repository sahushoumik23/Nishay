# MLOPs-task-3

The world has always seen what Machine Learning can achieve...The miracles that Data Scientists create with  their codes.

These programmers actually think and then make the models creted in ML accurate...

But what if we create a system that can run a model, retrain the model and make it accurate on its own...In short, automate the whole process a person does manually...

But is it possible with Machine Learning???

No, its not but with integration of DevOps it surely is....Thereby forming Ml+DevOps=MLOps

<h1>Just some Tasks are needed to be done...</h1>

<ul>
  <li>First task is to create a Dockerfile that will help us with creating an image with most of the required libraries installed..
    
   ![](Images/Dockerfile.png)
   
            FROM centos

            RUN yum install python3 -y

            RUN pip3 install --upgrade pip

            RUN pip3 install keras

            RUN pip3 install tensorflow

            RUN pip3 install numpy 

            RUN pip3 install pandas

            RUN pip3 install scipy

            RUN pip3 install opencv-python

            RUN pip3 install sklearn 
            
   Now we build the image using the build command:
   
   ![](Images/Dockerbuild_syntax.png)
   
   In my case I used : 
   
   ![](Images/docker_build.png)
   
   Now the image is built</li>
   
   <li>To achieve the automation..we use the Jenkins that will run a set of jobs..
      <ul>
        <li><h2>First Job</h2>
          <h4>This Job simply just copies all files in GitHub repo to the local machine...
            
        </li>
  </ul>
   
   
   
   
    
 
