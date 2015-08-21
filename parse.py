import github3 

import re, sys, time, getpass
from string import strip

gh_user = raw_input("User: ")
gh_pass = getpass.getpass()

gh = github3.login(username=gh_user, password=gh_pass)

f = open('awesome-javascript/README.md')
output_file = open('README_new.md', 'w')

for line in f:
    m = re.search(r"http(s)?://.*github.com/(?P<owner>[\w.-]+)/(?P<repo>[\w.-]+)", line)

    if m:
        # Obtain the project name
        owner = m.group('owner')
        repo = m.group('repo')

        # Get star number of project
        r = gh.repository(owner, repo)
        stars = r.stargazers

        # Print out the result
        print >>output_file, "{} [**{:,}**]".format(strip(line), stars)
        print "{} [**{:,}**]".format(strip(line), stars)

        # Throttle the speed
        time.sleep(0.5)
    else:
        print >>output_file, strip(line)
        print strip(line)
