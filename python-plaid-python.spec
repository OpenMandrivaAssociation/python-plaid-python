Name:		python-plaid-python
Version:	7.2.1
Release:	1
Summary:	Python client library for the Plaid API and Link
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/plaid-python/
Source0:	plaid-python-7.2.1.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
Python client library for the Plaid API and Link.

%files
%{py_sitedir}/*
