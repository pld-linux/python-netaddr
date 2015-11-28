#
# Conditional build:
%bcond_without	apidocs	# sphinx based documentation
%bcond_without	python3		# do not build python3 modules

%define		module	netaddr
Summary:	A pure Python network address representation and manipulation library
Name:		python-netaddr
Version:	0.7.14
Release:	3
License:	BSD
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/n/netaddr/%{module}-%{version}.tar.gz
# Source0-md5:	1ba9d1e887c838f190774cf6b74c109d
URL:		https://github.com/drkjam/netaddr/
BuildRequires:	python-modules
%{?with_python3:BuildRequires:	python3-modules}
BuildRequires:	rpm-pythonprov
%{?with_apidocs:BuildRequires:	sphinx-pdg}
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

%package -n python3-netaddr
Summary:	A pure Python network address representation and manipulation library
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

%package -n netaddr
Summary:	An interactive shell for the Python netaddr library
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description -n netaddr
Interactive shell for the python-netaddr library.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%if %{with apidocs}
sphinx-build -b html -d build/doctrees -D latex_paper_size=a4 docs/source build/html
%endif

%if %{with python3}
%py3_install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%py3_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py3_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README THANKS
%if %{with apidocs}
%doc build/html
%endif
%{py_sitescriptdir}/*.egg-info
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/eui
%{py_sitescriptdir}/%{module}/eui/*.py[co]
%{py_sitescriptdir}/%{module}/eui/*.idx
%{py_sitescriptdir}/%{module}/eui/*.txt
%dir %{py_sitescriptdir}/%{module}/ip
%{py_sitescriptdir}/%{module}/ip/*.py[co]
%{py_sitescriptdir}/%{module}/ip/*.xml
%dir %{py_sitescriptdir}/%{module}/strategy
%{py_sitescriptdir}/%{module}/strategy/*.py[co]
%dir %{py_sitescriptdir}/%{module}/tests
%{py_sitescriptdir}/%{module}/tests/*.py[co]
#%{py_sitescriptdir}/%{module}/tests/2.x/core
#%{py_sitescriptdir}/%{module}/tests/2.x/eui
#%{py_sitescriptdir}/%{module}/tests/2.x/ip
#%{py_sitescriptdir}/%{module}/tests/2.x/strategy

%if %{with python3}
%files -n python3-netaddr
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README THANKS
%if %{with apidocs}
%doc build/html
%endif
%{py3_sitescriptdir}/*.egg-info
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%dir %{py3_sitescriptdir}/%{module}/eui
%{py3_sitescriptdir}/%{module}/eui/*.py
%{py3_sitescriptdir}/%{module}/eui/__pycache__
%{py3_sitescriptdir}/%{module}/eui/*.idx
%{py3_sitescriptdir}/%{module}/eui/*.txt
%dir %{py3_sitescriptdir}/%{module}/ip
%{py3_sitescriptdir}/%{module}/ip/*.py
%{py3_sitescriptdir}/%{module}/ip/__pycache__
%{py3_sitescriptdir}/%{module}/ip/*.xml
%dir %{py3_sitescriptdir}/%{module}/strategy
%{py3_sitescriptdir}/%{module}/strategy/*.py
%{py3_sitescriptdir}/%{module}/strategy/__pycache__
%dir %{py3_sitescriptdir}/%{module}/tests
%{py3_sitescriptdir}/%{module}/tests/*.py
%{py3_sitescriptdir}/%{module}/tests/__pycache__
#%{py3_sitescriptdir}/%{module}/tests/3.x/core
#%{py3_sitescriptdir}/%{module}/tests/3.x/eui
#%{py3_sitescriptdir}/%{module}/tests/3.x/ip
#%{py3_sitescriptdir}/%{module}/tests/3.x/strategy
%endif

%files -n netaddr
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/netaddr
