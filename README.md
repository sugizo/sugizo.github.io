# Link
[Web] (https://sugizo.github.io/){target="_blank"}  
[Awards] (https://sugizo.github.io/awards/){target="_blank"}  
[Certificates] (https://sugizo.github.io/certificates/){target="_blank"}  
[Resume] (https://sugizo.github.io/resume/){target="_blank"}  

# Clone the repository
	cd ~/git/github
	git clone https://github.com/sugizo/sugizo.github.io

# Create File
	cd ~/git/github/sugizo.github.io

# Add, commit, and push your changes
	git gc --prune=1.day.ago
	git add --all
	git commit -m "Initial Commit"
	git push -uf origin master
	git gc --prune=1.day.ago

# Add, commit, and push your changes
	git gc --prune=1.day.ago
	git add --all
	git commit -m "v0.0"
	git tag v0.0
	git tag
	git push -u origin master
	git push origin --tags
	git gc --prune=1.day.ago
