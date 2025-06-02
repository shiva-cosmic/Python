# Write a program to find out whether a given post is talking about "Shivansh" or not. (In anyform lower, upper case )
post = input("Enter the post:")

if ("Shivansh".lower() in post.lower() ):
  print("this post is talking about shivansh")
else:
   print("this post is not talking about shivansh")