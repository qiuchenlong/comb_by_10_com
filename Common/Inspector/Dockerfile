# The FROM instruction sets the Base Image for subsequent instructions.
# Using Nginx as Base Image
FROM nginx:1.9
MAINTAINER Irisa Wang <angewsy1007@d163.com>


# Adding HelloWorld page into Nginx server
COPY . /usr/share/nginx/html

# The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime
EXPOSE 80

# The CMD instruction provides default execution command for an container
# Start Nginx and keep it from running background
CMD ["nginx", "-g", "daemon off;"]
