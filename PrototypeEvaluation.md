## The Idea

Our goal was to create an interface that would allow a user to choose a set of filters or search criteria, and search a cloud-stored dataset for matches. This would be specifically designed to work with STAC compliant data catalogs, and search the various attributes associated with geo-spatial images as defined by the specification.

To accomplish this, we sought to have our application use an online query language (MongoDB) to generate a query which would then be run on Google Cloud Platform (GCP), where the data would also stored.

We were able to emulate this functionality locally, with a small data sample hosted with MongoDB. However our attempts to execute this at full scale on the GCP app engine resulted in a failure to access the data. Due to our inexperience with serverless architecture and a lack of time available, we were unable to overcome this by the project deadline. We believe the issue to be firewall related, but were unable to find any online documentation on how to work around this.

Despite this result, we believe our concept to be viable. We have seen other examples of MongoDB queries run on cloud architecture, and our own successful local implementation confirms that we were able to construct MongoDB queries that work with STAC formatted data, and execute them using our own interface.

## Scalability

Unfortunately, we are unable to realistically assess the scalability of our project. Its ability to work with large, continuously growing datasets was entirely dependant our ability to take our local implementation and execute it on the Google Cloud Platform. 

From a theoretical perspective, we can speculate that had we been able to solve the firewall issue, there should be no difficulties running our queries on a much larger, dynamic dataset, assuming that it adheres to the STAC specification. The only downside of scaling this way should be increased computational work. Additionally, we believe that computational costs associated with each query would remain extremely low, even with extremely large datasets. Yet, we are unable to conclusively measure this as we do not have a successful cloud-based run from which to extrapolate.

## Evolution

Because serverless architecture is still so new, and in the infancy of its adoption, the evolutionary needs may be tremendous. While we intentionally kept the scope of our project narrow (to focus on STAC-compliant geo-spatial datasets), it must be anticipated that users of our product will have needs we have not yet anticipated.

Additionally, because our project is so specifically focused on the STAC data format, we live and die by the adoption of this specification. If for some reason STAC becomes replaced by another data format, our entire codebase must be adapted or discarded.

Yet, if we operate under the assumption that our technical hurdle can be overcome, and pretend that we were able to run our query on GCP and not just locally, there is reason to believe this application could continue to evolve and be useful well into the future.

Even if the STAC specification were abandoned in favor of another way of indexing geo-spatial data, the new format would have to store all of the relevant attributes in an accessible searchable format, and it isn’t a stretch to assume that it wouldn’t require much rework to adapt our search utility to a new format. On that note, it is also worth considering that our query engine could therefore also be expanded to work with other datasets entirely.

Importantly, we have been rigorous in our adoption of both our continuous integration tool (Travis CI in tandem with GitHub) and our continuous integration tool (Google Cloud Platform). Because of this, our code development has been thoroughly version-controlled, and has grown with minimal increase in code complexity, and managed to avoid the prominent anti-patterns that could threaten maintainability and evolvability.
