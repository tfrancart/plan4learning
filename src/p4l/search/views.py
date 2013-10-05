# -*- coding: utf-8 -*-
#
# Copyright IRI (c) 2013
#
# contact@iri.centrepompidou.fr
#
# This software is governed by the CeCILL-B license under French law and
# abiding by the rules of distribution of free software.  You can  use, 
# modify and/ or redistribute the software under the terms of the CeCILL-B
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info". 
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability. 
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or 
# data to be ensured and,  more generally, to use and operate it in the 
# same conditions as regards security. 
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL-B license and that you accept its terms.
#


from django.conf import settings
from django.template.context import RequestContext
from haystack.query import SearchQuerySet
from haystack.views import SearchView, search_view_factory

from p4l.search.forms import RecordSearchForm


class RecordSearchView(SearchView):
    
    def __init__(self, template=None, load_all=True, form_class=None, searchqueryset=None, context_class=RequestContext, results_per_page=None):
        record_searchQuerySet = SearchQuerySet().order_by('identifier')
        template = "p4l/home.html"
        results_per_page= settings.NB_RECORDS_BY_PAGE
        form_class = RecordSearchForm
        SearchView.__init__(self, template=template, load_all=False, form_class=form_class, searchqueryset=record_searchQuerySet, context_class=context_class, results_per_page=results_per_page)

    @classmethod
    def as_view(cls):
        return search_view_factory(view_class=cls)