Introduction

We had several concerns relating to maintenance and evolutions with this project. While typical problems such as scaling and technological obsolescence were covered by the cloud platform, we would be establishing a system that would potentially be built upon and updated by people without a computer science or software engineering background. Clearly a strong foundation, with good documentation and tools would be needed to protect the future growth potential of the project.

Primary among our concerns were the first two laws, as defined by Lehman:

Law of continuous change
Law of increasing complexity

In order for our query/filter engine to continue to be useful long after our role in the project completed, it would have to be able to adapt as users needs adapted.

From an adoption perspective, we are still in the infancy of cloud computing. While there are some obvious candidates already making the transition (eg: algorithms that work with huge datasets), the extent to which adoption will be widespread is still unknown, but will certainly be an increase over the current level. With that in mind, basic framework for working in a cloud environment - of which our project is one example - will likely need to constantly expand in scope to accommodate new demands, or risk being replaced by more versatile offerings.

Re-Engineering Querying of STAC data

In our deep dive into the STAC data format, we found a surprisingly lack of support for basic functions such as querying and filtering of large datasets using serverless architecture. While such functions are abundant and trivial for normal databases using a single server, it was clear that there was a need to repurpose these basic processes for use with a new environment.

To this end, we chose to use MongoDB, which allowed us to use a familiar database query structure, but applied to a cloud-based dataset and executed on a serverless platform.

Rather than a conventional database structure as seen below:


We would be orchestrating a cooperative effort between MongoDB and the Google Cloud, to generate and execute a query. Ideally, our application would make as much of this happen behind-the-scenes as possible, but the time constraints of the project required some degree of compromise.



Continuous integration

Continuous integration tools have tremendous value for software projects that involve multiple contributors. Frequent updates to a shared repository helps to eliminate redundant work and conflicts. Automated processes can detect errors, run automated tests, and provide immediate feedback.

We chose Travis CI - and by extension - GitHub as our CI tool. The wide adoption of GitHub maximized the chance that future users would be familiar with the repository, and ensured that there exists an abundance of tutorials and support. Additionally, Travis CI had a free option, which was a requirement for us.

Travis CI offered some advantages over simply using GitHub alone. It can be configured to alert all contributors whenever new commits are pushed, or a pull request is submitted. These alerts can take many forms, for example email, and help keep all contributors updated on work done by others, and the overall progress of the project.


Configuration Management

Given that our project was to run on Google Cloud, we clearly needed some performance monitoring and management, lest a stray infinite loop destroy our entire budget. Additionally, the efficiency of our search and query algorithm could become increasingly important as it gets used to work with perpetually scaling datasets.

Google Cloud Platform itself served as our configuration management tool. It provided active monitoring of all running jobs, flags for any issues, and the ability to kill a job remotely. Additionally, it was able to directly access our GitHub code repository, and update or rollback versions as needed. Compared to typical expectations for configuration management software, this was relatively painless to setup and use.

Maintenance and Evolution

By establishing the importance of both our CI and CM tools in the developmental stages of our project, we have given it the maximum possible chance of survival beyond its initial release. Given the absolute certainty of Law 1 (the law of continuous change) with respect to both the utility and the scope of our project, which is a result of this being a timid first step into a vast unexplored realm, it is our hope that all future development will embrace the tools and techniques that we have used and continue them going forward.
