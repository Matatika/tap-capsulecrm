"""Stream type classes for tap-capsulecrm."""

from singer_sdk import typing as th

from tap_capsulecrm.client import CapsulecrmStream


class PartiesStream(CapsulecrmStream):
    """Define Parties stream."""

    name = "parties"
    path = "/parties"
    primary_keys = ["id"]
    replication_key = "updatedAt"
    records_jsonpath = "$.parties[*]"
    schema = th.PropertiesList(
        th.Property("id", th.NumberType),
        th.Property("type", th.StringType),
        th.Property("about", th.StringType),
        th.Property("title", th.StringType),
        th.Property("firstName", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("jobTitle", th.StringType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
        th.Property(
            "organisation",
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("pictureURL", th.StringType),
                th.Property("username", th.StringType),
            ),
        ),
        th.Property("lastContactedAt", th.DateTimeType),
        th.Property(
            "owner",
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("pictureURL", th.StringType),
                th.Property("username", th.StringType),
            ),
        ),
        th.Property("team", th.StringType),
        th.Property(
            "addresses",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.NumberType),
                    th.Property("type", th.StringType),
                    th.Property("city", th.StringType),
                    th.Property("country", th.StringType),
                    th.Property("street", th.StringType),
                    th.Property("state", th.StringType),
                    th.Property("zip", th.StringType),
                )
            ),
        ),
        th.Property(
            "phoneNumbers",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.NumberType),
                    th.Property("type", th.StringType),
                    th.Property("number", th.StringType),
                )
            ),
        ),
        th.Property(
            "websites",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.NumberType),
                    th.Property("type", th.StringType),
                    th.Property("address", th.StringType),
                    th.Property("service", th.StringType),
                    th.Property("url", th.StringType),
                ),
            ),
        ),
        th.Property(
            "emailAddresses",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.NumberType),
                    th.Property("type", th.StringType),
                    th.Property("address", th.StringType),
                ),
            ),
        ),
        th.Property("pictureURL", th.StringType),
    ).to_dict()


class OpportunitiesStream(CapsulecrmStream):
    """Define Opportunities stream."""

    name = "opportunities"
    path = "/opportunities"
    primary_keys = ["id"]
    replication_key = "updatedAt"
    records_jsonpath = "$.opportunities[*]"
    schema = th.PropertiesList(
        th.Property("id", th.NumberType),
        th.Property("updatedAt", th.DateTimeType),
        th.Property("description", th.StringType),
        th.Property(
            "owner",
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("name", th.StringType),
                th.Property("pictureURL", th.StringType),
                th.Property("username", th.StringType),
            ),
        ),
        th.Property(
            "party",
            th.ObjectType(
                th.Property("id", th.NumberType),
                th.Property("username", th.StringType),
                th.Property("name", th.StringType),
            ),
        ),
        th.Property("lostReason", th.StringType),
        th.Property(
            "milestone",
            th.ObjectType(
                th.Property("id", th.NumberType),
                th.Property("name", th.StringType),
            ),
        ),
        th.Property(
            "value",
            th.ObjectType(
                th.Property("amount", th.NumberType),
                th.Property("currency", th.StringType),
            ),
        ),
        th.Property("expectedCloseOn", th.DateTimeType),
        th.Property("probability", th.NumberType),
        th.Property("durationBasis", th.StringType),
        th.Property("duration", th.StringType),
        th.Property("closedOn", th.StringType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("name", th.StringType),
    ).to_dict()


class ProjectsStream(CapsulecrmStream):
    """Define Projects stream."""

    name = "projects"
    path = "/kases"
    primary_keys = ["id"]
    replication_key = "updatedAt"
    records_jsonpath = "$.kases[*]"
    schema = th.PropertiesList(
        th.Property("id", th.NumberType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
        th.Property("status", th.StringType),
        th.Property("name", th.StringType),
        th.Property("description", th.StringType),
        th.Property("closedOn", th.StringType),
        th.Property("expectedCloseOn", th.DateTimeType),
        th.Property("lastContactedAt", th.DateTimeType),
        th.Property(
            "team",
            th.ObjectType(
                th.Property("id", th.IntegerType),
            ),
        ),
        th.Property(
            "opportunity",
            th.ObjectType(
                th.Property("id", th.IntegerType),
            ),
        ),
        th.Property(
            "owner",
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("deleted", th.BooleanType),
                th.Property("name", th.StringType),
                th.Property("pictureURL", th.StringType),
                th.Property("username", th.StringType),
            ),
        ),
        th.Property(
            "party",
            th.ObjectType(
                th.Property("id", th.NumberType),
                th.Property("type", th.StringType),
                th.Property("name", th.StringType),
                th.Property("pictureURL", th.StringType),
            ),
        ),
        th.Property(
            "stage",
            th.ObjectType(
                th.Property("id", th.NumberType),
                th.Property("name", th.StringType),
            ),
        ),
        th.Property(
            "tags",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.NumberType),
                    th.Property("name", th.StringType),
                    th.Property("dataTag", th.BooleanType),
                ),
            ),
        ),
        th.Property(
            "fields",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.NumberType),
                    th.Property(
                        "definition",
                        th.ObjectType(
                            th.Property("id", th.NumberType),
                            th.Property("name", th.StringType),
                        ),
                    ),
                    th.Property("value", th.AnyType),
                    th.Property("tagId", th.NumberType),
                ),
            ),
        ),
    ).to_dict()

    def get_url_params(self, context, next_page_token):
        params = super().get_url_params(context, next_page_token)
        params["embed"] = ",".join(["tags", "fields"])

        return params
