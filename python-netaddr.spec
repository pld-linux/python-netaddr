%define		module	netaddr
Summary:	A pure Python network address representation and manipulation library
Name:		python-netaddr
Version:	0.7.3
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://netaddr.googlecode.com/files/netaddr-%{version}.tar.gz
# Source0-md5:	8b7b574bca2f60722ccd90c71334ee32
URL:		http://code.google.com/p/netaddr/
BuildRequires:	python-devel
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

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/api AUTHORS CHANGELOG README THANKS
%attr(755,root,root) %{_bindir}/netaddr
%{py_sitescriptdir}/*.egg-info
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/eui
%{py_sitescriptdir}/%{module}/eui/*.py[co]
%{py_sitescriptdir}/%{module}/eui/*.idx
%{py_sitescriptdir}/%{module}/eui/*.txt
%dir %{py_sitescriptdir}/%{module}/ip
%{py_sitescriptdir}/%{module}/ip/*.py[co]
%{py_sitescriptdir}/%{module}/ip/*-space
%{py_sitescriptdir}/%{module}/ip/*-addresses
%dir %{py_sitescriptdir}/%{module}/strategy
%{py_sitescriptdir}/%{module}/strategy/*.py[co]
%dir %{py_sitescriptdir}/%{module}/tests
%{py_sitescriptdir}/%{module}/tests/*.py[co]
%{py_sitescriptdir}/%{module}/tests/core
%{py_sitescriptdir}/%{module}/tests/eui
%{py_sitescriptdir}/%{module}/tests/ip
%{py_sitescriptdir}/%{module}/tests/strategy
