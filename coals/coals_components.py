#!/usr/bin/python3
#
# Copyright 2018 British Broadcasting Corporation
#
# Author: Michael Sparks <michael.sparks@bbc.co.uk>
#
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from ecs_core.ecs_core import mkComponent


# Components used in Concepts
Concept = mkComponent("Concept", "logical_id") # LogicalID 
Description = mkComponent("Description", "description")
Depends = mkComponent("Depends", "depends")
Suggests = mkComponent("Suggests", "suggests")
NGramDecay = mkComponent("NGramDecay", "decay_type", "amount", "when")
SecureLevel = mkComponent("SecureLevel", "secure")
IdealLevel= mkComponent("IdealLevel", "ideal")
LongDescription = mkComponent("LongDescription", "longdescription")
Notes = mkComponent("Notes", "notes")


# Components used in Resources
Resource = mkComponent("Resource", "logical_id")
Title = mkComponent("Title", "title")
Name = mkComponent("Name", "name")
Url = mkComponent("Url", "url")
CoversConcept = mkComponent("CoversConcept", "concept")
NGramDelta = mkComponent("NGramDelta", "op", "ngram", "delta")
NGramConstraint = mkComponent("NGramConstraint", "op","ngram", "level")
DependsResource = mkComponent("DependsResource", "depends_resource")
DateUpdated = mkComponent("DateUpdated", "date_updated")
Template = mkComponent("Template", "template")
SourceForm = mkComponent("SourceForm", "source_form")
ResourceSpecification = mkComponent("ResourceSpecification", "resource_specification")
ResourceContent= mkComponent("ResourceContent", "resource_content")

concept_components = [Concept, Description, Depends, Suggests, NGramDecay, SecureLevel, IdealLevel, LongDescription, Notes]

resource_components = [Resource, Title, Name, Url, CoversConcept, NGramDelta, 
                       NGramConstraint, DependsResource, DateUpdated, Template, 
                       SourceForm, ResourceSpecification, ResourceContent]

