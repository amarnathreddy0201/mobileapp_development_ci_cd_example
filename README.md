# mobileapp_development_ci_cd_example

 Changing the main repo in github Automatically CI/CD pipe line will run and update the code.
 AWS Lambda Services USing Fast API , AWS and GitHub CI/CD Pipe line.
 1) Don't add AWS Credintials in github it will block AWS Account.
 2) Go to project repo -> settings -> Secrect and Variables -> Action
 3) Add AWS CDredintials as below mentioned.
 4) In AWS Function, Function name we gonna change.
   
 https://github.com/amarnathreddy0201/mobileapp_development_ci_cd_example/blob/main/.github/workflows/main.yml
 
 AWS_ACCESS_KEY_ID: ${{ secrets.AWS_SECRET_ACCESS_KEY_ID }}
 AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
 AWS_DEFAULT_REGION: ${{ secrets.AWS_DEFAULT_REGION }}
