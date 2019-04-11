# Future Work based on these results: what additional issues need to be addressed in future iterations of your system?

In order for our project to be useful beyond its initial release, it must continue to evolve beyond its current function. However, it must always remain efficient, easy-to-use, and versatile. Most importantly, the integrity of the development process must be preserved, meaning there is an increased emphasis on the continued use of our DevOps tools, and our strategies for mitigating the risks of software evolution.

## Continued progress

Our initial goal was for our UI to shelter the user from the backend as much as possible. To this end, there are still features that could be added and would help improve the application’s usefulness, including:
```
Linking to any google cloud account to the UI
Supporting the uploading/downloading and editing of datasets and portions of datasets directly through the UI
Job status monitoring directly in the UI
Offering an interface to access the data links returned by a completed query
Ability to search nested folders
Improved scalability on the back-end
Automated unit testing integrated with the build process
```

## Future Evolution

As more and more software migrates to serverless architecture, other methods to search and filter large datasets will no doubt emerge. In order for our system to remain relevant it would offer utility beyond the ‘initial step’ we are currently offering.

In addition to allowing a user to directly run a query, offering this functionality as platform for other software would add a whole new purpose, or at least eliminate the need for repetitive user participation. For example, allowing a cloud-based algorithm to, as a sub-function of its own purpose, run a query using our engine, and then directly feed the results into its algorithm would streamline the process by eliminating manual input. Additionally, this would help support repeated querying, for example when a user wishes to process some data, and then run a query on the new modified data that was produced.

While we have chosen to focus on the STAC data format, specifically for geo-spatial data, there are many opportunities out there for other cloud-based datasets that may also be unsupported by conventional query systems. Increasing our reach by offering support to other formats could help the project grow and thrive.

## Risks

Competing offerings - due to the fundamental nature of our service, it is likely that others have had the same idea and may put out a superior solution

Live and die by the STAC - if the stac specification fails to become widely adopted, the need for our query solution will be compromised.

Importance of DevOps

While it is implied that serverless architecture should eliminate concerns related to scaling, there are laws of software evolution that can threaten the future of this project if ignored.

## GitHub and Travis CI

These tools have proven invaluable at keeping our team on the same page, and updated on each others’ progress. Without a tool for continuous integration, is it likely that many ugly anti-patterns will quickly emerge threatening the efficiency and maintainability of the project. In particular:
```
Lava Flow - this is extremely common when code is handed off from one team of contributors to another. Sections that new coders are unfamiliar with will remain untouched, yet unused, as the fear of ‘breaking something’ outweighs the desire to maintain readable maintainable code
Poltergeists - as above, but for entire classes
The Blob - this is commonly the results of lack of oversight and organisation, as one module ends up being continuously added to and doing the bulk of the work without appropriate segmentation.
```

There are many others that are relevant, but this short list highlights some of the biggest concerns for an evolving project such as this one. Coding for cloud architecture does not yet have widespread familiarity, and the likelihood of rapidly increasing code complexity along with insufficient modularity and documentation are at an even higher risk than normal, especially if the project is handed off to other coders less familiar with these concepts.

Additionally, due to the relative ‘newness’ of serverless architecture, there is still a great deal of unexplored territory. Our query system has been well-thought out for geospatial data that strictly follows a specified format. As hinted at in the future evolution section, if we were to consider broadening our querying ability to other datasets, there could arise numerous unforeseen issues that could require anything from minor adjustments to complete re-engineering of our core codebase.

All of this serves to reinforce the importance of the CI and CM tools. By following good coding practices and collaboration tools, complexity and maintainability creep can be minimized.
