# Auto generated from biobricks_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-04-04T07:41:34
# Schema: biobricks-schema
#
# id: https://w3id.org/biobricks-ai/biobricks-schema
# description: BioBricks data dictionary schema
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOBRICKS_SCHEMA = CurieNamespace('biobricks_schema', 'https://w3id.org/biobricks-ai/biobricks-schema/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = BIOBRICKS_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class BrickId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = BIOBRICKS_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Brick(NamedThing):
    """
    Represents a Brick
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOBRICKS_SCHEMA["Brick"]
    class_class_curie: ClassVar[str] = "biobricks_schema:Brick"
    class_name: ClassVar[str] = "Brick"
    class_model_uri: ClassVar[URIRef] = BIOBRICKS_SCHEMA.Brick

    id: Union[str, BrickId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BrickId):
            self.id = BrickId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass
class BrickCollection(YAMLRoot):
    """
    A holder for Brick objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOBRICKS_SCHEMA["BrickCollection"]
    class_class_curie: ClassVar[str] = "biobricks_schema:BrickCollection"
    class_name: ClassVar[str] = "BrickCollection"
    class_model_uri: ClassVar[URIRef] = BIOBRICKS_SCHEMA.BrickCollection

    entries: Optional[Union[Dict[Union[str, BrickId], Union[dict, Brick]], List[Union[dict, Brick]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Brick, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=BIOBRICKS_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=BIOBRICKS_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=BIOBRICKS_SCHEMA.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=BIOBRICKS_SCHEMA.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=BIOBRICKS_SCHEMA.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=BIOBRICKS_SCHEMA.age_in_years, name="age_in_years", curie=BIOBRICKS_SCHEMA.curie('age_in_years'),
                   model_uri=BIOBRICKS_SCHEMA.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=BIOBRICKS_SCHEMA.vital_status, name="vital_status", curie=BIOBRICKS_SCHEMA.curie('vital_status'),
                   model_uri=BIOBRICKS_SCHEMA.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.brickCollection__entries = Slot(uri=BIOBRICKS_SCHEMA.entries, name="brickCollection__entries", curie=BIOBRICKS_SCHEMA.curie('entries'),
                   model_uri=BIOBRICKS_SCHEMA.brickCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, BrickId], Union[dict, Brick]], List[Union[dict, Brick]]]])

slots.Brick_primary_email = Slot(uri=SCHEMA.email, name="Brick_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=BIOBRICKS_SCHEMA.Brick_primary_email, domain=Brick, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))