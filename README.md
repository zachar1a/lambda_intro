# lambda_intro

intro to aws lambda functions

Among other things, this lambda primarily will:

-   Step 1 - PlACE STEPS HERE


## Required AWS Artifacts

This process relies on the below AWS capabilities.

| Type                         | Name                                                   | Description                                                     |
| ---------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------|
| Lambda                       | lambda_intro-_\[ext\]_              | Orchestrates the delete docs automation                         |
| Resource Group               | lambda_intro-_\[ext\]_              | Resource group of all artifacts                                 |


## AWS Artifact Configuration Notes

### Resource Group

Resource group is tag based. Artifacts are matched where application is "kanan" and feature is "delete-docs"


## Environment Variable Definitions

The lambda makes use of the below environment variables.

| Key                                   | Component                  | Required? | Description                                                                                     |
| ------------------------------------- | -------------------------- | :-------: | ----------------------------------------------------------------------------------------------- |
| NEW_RELIC_ACCOUNT_ID                  | All                        |    Yes    | Used by New Relic Layer for logging                                                             |
| NEW_RELIC_DISTRIBUTED_TRACING_ENABLED | All                        |    Yes    | Used by New Relic Layer for logging                                                             |
| NEW_RELIC_SERVERLESS_MODE_ENABLED     | All                        |    Yes    | Used by New Relic Layer for logging                                                             |
| environment                           | All                        |    Yes    | Used by lambda                                                                                  |

## Environment Variable Values

Below lists variables whose values do not vary by environment:

| Key                                   | Value                                |
| ------------------------------------- | ------------------------------------ |
| NEW_RELIC_DISTRIBUTED_TRACING_ENABLED | true                                 |
| NEW_RELIC_SERVERLESS_MODE_ENABLED     | true                                 |
| environment                           | current environment (ie development) |

Below lists variables whose values **do** vary by environment:

| Key                      | Dev Stage                                                         |
| ------------------------ | ----------------------------------------------------------------- |
| NEW_RELIC_ACCOUNT_ID     | 399786                                                            |

