# Movie Catalogue and Favourites Backend

**Java · Spring Boot · MyBatis · Vue 2 · Element UI · RuoYi**

## Overview

This project provides backend services and an administration interface for organising movie metadata. It supports browsing and filtering a catalogue, maintaining actor/director relationships, managing favourites and exporting records for review.

The portfolio emphasises backend work. The supplied source also contains a Vue administration interface; its presence does not establish individual authorship of every frontend component.

## Functionality supported by the source

| Capability | Implementation evidence in the original archive |
|---|---|
| Filtered movie queries | `movie-data/src/main/java/com/movie/data/controller/MoviesController.java`, method `list` |
| Pagination and record retrieval | `movie-data/src/main/java/com/movie/data/service/impl/MoviesServiceImpl.java`, method `selectMoviesList` |
| Movie-to-actor/director relationships | `movie-data/src/main/resources/mapper/movies/MoviesMapper.xml` and movie controller add/edit flows |
| Add, retrieve and remove favourites | `movie-data/src/main/java/com/movie/data/controller/CollectionsController.java` |
| Favourites persistence | `movie-data/src/main/resources/mapper/collectors/CollectionsMapper.xml` |
| Export enriched movie records to Excel | `MoviesController.java`, method `export` |
| Movie administration screen | `movie-ui/src/views/movies/movies/index.vue` |

Paths above are relative to the `movie/` directory in the original archive. They are evidence references, not links to published source files.

## A request through the system

1. The interface supplies movie and filtering parameters to the list endpoint.
2. The controller builds filter parameters and passes them to the service.
3. The service obtains matching movie IDs, selects the requested page in memory and loads related movie records through MyBatis.
4. The controller returns a structured response containing rows and a total count.
5. A separate export flow converts movie records into export objects and includes readable region, genre, actor and director information.

## Engineering discussion

The project offers concrete examples of controller/service/mapper separation, relational data modelling and integration with an existing framework. It also provides useful opportunities for further work:

- Move pagination into the database for larger catalogues; the current service first loads matching IDs.
- Validate pagination inputs and exercise empty-result and boundary cases.
- Use POST/DELETE for favourites mutations instead of the current GET endpoints, and bind ownership checks to the authenticated user.
- Review transaction boundaries for movie updates spanning multiple related tables.

These are proposed improvements, not completed changes.

## Demonstration plan

A short recording can show: a catalogue query, a change of filters, a movie with related actor/director metadata, a favourites add/remove flow and an Excel export. Use sample records and a demonstration account. A recording has not yet been produced.

## Scope and attribution

The source is based on RuoYi. Framework infrastructure and generated CRUD code should retain their original attribution. The available archive supports this backend case study, but does not yet substantiate the collaborative-filtering component described in the earlier CV. No accuracy, latency, user-count or production-readiness claims are made.

## Validation status

Static source inspection completed on 10 November 2026. The full application has not been built or run for this portfolio review. A reproducible deployment and an executable demo remain separate tasks.
