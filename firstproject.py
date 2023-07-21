import instaloader
ins = instaloader.Instaloader()
profile_input = input("Enter user name")
# ins.download_profile(profile_input=True)
print("download media....")
ins.download_profile(profile_input, profile_pic=False)
print("download  successful")
