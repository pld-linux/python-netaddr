#
# Conditional build:
%bcond_without	doc		# Sphinx based documentation
%bcond_without	tests		# unit tests
%bcond_without	python2		# CPython 2.x modules
%bcond_without	python3		# CPython 3.x modules

%define		module	netaddr
Summary:	A pure Python network address representation and manipulation library
Summary(pl.UTF-8):	Czysto pythonowa biblioteka do reprezentacji i operacji na adresach sieciowych
Name:		python-netaddr
Version:	0.10.1
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/n/netaddr/%{module}-%{version}.tar.gz
# Source0-md5:	c0d7b080da18c851ea436389813d7652
Patch0:		netaddr-coding.patch
URL:		https://github.com/drkjam/netaddr/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
%if %{with tests}
BuildRequires:	python-importlib_resources
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	rpm-pythonprov
%{?with_doc:BuildRequires:	sphinx-pdg-3}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pure Python network address representation and manipulation library.

netaddr provides a Pythonic way to work with:
- IPv4 and IPv6 addresses and subnets (including CIDR notation)
- MAC (Media Access Control) addresses in multiple presentation
  formats
- IEEE EUI-64, OUI and IAB identifiers
- nmap-style IP address ranges
- a user friendly IP glob-style format

Included are routines for:
- generating, sorting and summarizing IP addresses
- converting IP addresses and ranges between various different formats
- performing set based operations on groups of IP addresses and
  subnets
- arbitrary IP address range calculations and conversions
- querying IEEE OUI and IAB organisational information
- querying of IP standards related data from key IANA data sources

%description -l pl.UTF-8
Czysto pythonowa biblioteka do reprezentacji i operacji na adresach
sieciowych.

Zapewnia pythonowe sposoby pracy z:
- adresami i podsieciami IPv4 i IPv6 (wraz z notacją CIDR)
- adresami MAC (Media Access Control) w wielu formatach
- identyfikatorami IEEE EUI-64, OUI i IAB
- przedziałami adresów IP w stylu nmapa
- przyjaznym dla użytkownika formacie IP w stylu globów

Zawiera funkcje do:
- generowania, sortowania i skracania adresów IP
- konwersji adresów i przedziałów IP między różnymi formatami
- operacji teoriomnogościowych na grupach adresów i podsieciach IP
- dowolnych obliczeń i konwersji przedziałów adresów IP
- zapytań o informacje organizacyjne dotyczące IEEE OUI i IAB
- zapytań o dane związane ze standardami IP z kluczowych źródeł IANA

%package -n python3-netaddr
Summary:	A pure Python network address representation and manipulation library
Summary(pl.UTF-8):	Czysto pythonowa biblioteka do reprezentacji i operacji na adresach sieciowych
Group:		Development/Languages/Python

%description -n python3-netaddr
A pure Python network address representation and manipulation library.

netaddr provides a Pythonic way to work with:
- IPv4 and IPv6 addresses and subnets (including CIDR notation)
- MAC (Media Access Control) addresses in multiple presentation
  formats
- IEEE EUI-64, OUI and IAB identifiers
- nmap-style IP address ranges
- a user friendly IP glob-style format

Included are routines for:
- generating, sorting and summarizing IP addresses
- converting IP addresses and ranges between various different formats
- performing set based operations on groups of IP addresses and
  subnets
- arbitrary IP address range calculations and conversions
- querying IEEE OUI and IAB organisational information
- querying of IP standards related data from key IANA data sources

%description -n python3-netaddr -l pl.UTF-8
Czysto pythonowa biblioteka do reprezentacji i operacji na adresach
sieciowych.

Zapewnia pythonowe sposoby pracy z:
- adresami i podsieciami IPv4 i IPv6 (wraz z notacją CIDR)
- adresami MAC (Media Access Control) w wielu formatach
- identyfikatorami IEEE EUI-64, OUI i IAB
- przedziałami adresów IP w stylu nmapa
- przyjaznym dla użytkownika formacie IP w stylu globów

Zawiera funkcje do:
- generowania, sortowania i skracania adresów IP
- konwersji adresów i przedziałów IP między różnymi formatami
- operacji teoriomnogościowych na grupach adresów i podsieciach IP
- dowolnych obliczeń i konwersji przedziałów adresów IP
- zapytań o informacje organizacyjne dotyczące IEEE OUI i IAB
- zapytań o dane związane ze standardami IP z kluczowych źródeł IANA

%package -n netaddr
Summary:	An interactive shell for the Python netaddr library
Summary(pl.UTF-8):	Interaktywna powłoka do biblioteki Pythona netaddr
Group:		Development/Languages/Python
%if %{with python3}
Requires:	python3-netaddr = %{version}-%{release}
%else
Requires:	%{name} = %{version}-%{release}
%endif

%description -n netaddr
Interactive shell for the python-netaddr library.

%description -n netaddr -l pl.UTF-8
Interaktywna powłoka do biblioteki Pythona netaddr.

%package apidocs
Summary:	API documentation for Python netaddr module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona netaddr
Group:		Documentation

%description apidocs
API documentation for Python netaddr module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona netaddr.

%prep
%setup -q -n %{module}-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python} -m pytest netaddr/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest netaddr/tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
sphinx-build-3 -b html docs/source docs/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%if %{with python3}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/*
%endif
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG COPYRIGHT LICENSE README.rst
%{py_sitescriptdir}/netaddr
%{py_sitescriptdir}/netaddr-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-netaddr
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG COPYRIGHT LICENSE README.rst
%{py3_sitescriptdir}/netaddr
%{py3_sitescriptdir}/netaddr-%{version}-py*.egg-info
%endif

%files -n netaddr
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/netaddr

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_modules,_static,dev-how-to,reference,*.html,*.js}
%endif
