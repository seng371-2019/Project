[![Build status](https://travis-ci.org/seng371-2019/travis-lab.svg?master)](https://travis-ci.org/seng371-2019)

## Team Members:
```
Oliver Lewis - V00877996
Eric May - V00867590
Tyler Drover - V00845692
Reece Pretorius - V00880300
Jesse Browell - V00873161
```
___
# Project 2 Outline
## Part 1: Project Breakdown
For this project our group is going to build a proof of concept for a STAC Spec search engine. We want to show how someone might go about searching through a large dataset that conforms to the STAC specification. Our system will be able to search through large volumes of STAC data located on a cloud based service. For the implimentation we are utilizing a variety of tools (Part 6) in the hopes of convincing the developers building the Earth Observation Platform that they need to use the right tools. We have broken down the project into the following tasks:

Milestone 1: Create Tool and Dataset Familiarity - March 11th | Milestone 2: Configure Build Process - March 18th | Milestone 3: Generalize STAC use case and search - March 18 | Milestone 4: Build implementation modules Due: March 28 | Milestone 5: Compile Project - March 30
--- | --- | --- | --- | ---
Azure Research | Define Azure Requirements | Findout what form of datasets users are looking for | User Interface | Link UI, Search Function, and Dataset
Jenkins Research | Outline automation proccess with GitHub, Puppet, and Jenkins | Outline how to search through STAC Spec | Search Function | Testing
Puppet Research | Configure System | | STAC dataset on cloud |
Acquire STAC compliant data | | | |

## Part 2: Approach
The approach our group will be taking for this project is is to break it down into smaller millestones consisting of research, design, development, and testing tasks. Many of the the inital research and design that must be down will require a whole team effort so that everone is on the same page, however, once the inital research phaze is over then we can work on individual tasks. For the coding and testing tasks, each task can be assigned to one or two group members to speed up the development time. Once the final testing has been completed, then we will get together once more as a group and finish the final report which is due. The timeline which we will follow is outlined below. 

Since, for many of the technologies we have limited knowladge of how they work and are implemented, communication will be critical throughout the project. In order to ensure that communication is maintained throughout, our group will rely heavily on Slack.
 
## Part 3: Team Structure
 Team Member | Role
 --- | ---
 Oliver Lewis | Scrum Master
 Eric May | STAC Guru
 Tyler Drover | Backend Developer
 Reece Pretorius | Frontend Developer
 Jesse Browell | DevOps
 
## Part 4: Timeline
For this project, we have broken down the parts into 5 different milestones over the course of the month. The first milestone is mostly planning and gaining familiarity with the tools in our project. Because the tools we are using are new to our team members, we have scheduled time to become familiar with these tools and plan exactly how they are used. Azure, Jenkins and Puppet are all fairly complicated tools and having an idea of how they will be implemented into our project will make development much more smooth. During this time period we will also acquire STAC compliant data to use in our project. We currently plan to have milestone 1 done by March 11th. 

For milestone two and three we will be building on the planning done in the first. In the second milestone, we plan to get the specifics of how the tools will be implemented. The exact requirements needed to use Azure in our project, an outline for the automation using GitHub, Puppet and Jenkins, and any configurations for our system will all be decided in this phase. Milestone three will have the team begin working with STAC compliant data. This is where we will create an outline on how to search through STAC spec and become more familiar with datasets used by researchers. Both milestones 2 and 3 will be finished by March 18th.

The fourth and fifth milestones are where we will implement our ideas and build the project. Milestone four is where we will begin creating the project. This phase is where we will develop modules for things such as the User Interface, the search function and the ability to store data in the cloud. In the fifth milestone, we will begin connecting these modules and make sure that they work together. This is also the milestone where we will do testing to catch any bugs that could exist. Milestone 4 is expected to be done on March 28th and Milestone 5 on March 30th.

 
## Part 5: Risks
The largest risks that our group will face with this project is the overall scope and time managment. Since we are exploring new technologies, it is easy for our group to scope out a project which we will not be able to accomplish as the complexity is to great or the timeline is to short. We also put ourselves at risk of picking the wrong tools at the offset of the project, agian since we have little expirence with these technologies. Without a large understanding of the domain which we are working in, it is difficult to initally create a structure for the project as well as set up timelines and scope for tasks. 
 
## Part 6: Tools Used
Version Control: GitHub

Automation: Jenkins

Configuration Management: Puppet

Cloud Platform: Microsoft Azure

Communication: Slack
