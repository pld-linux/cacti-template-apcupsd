%define		template apcupsd
%define		php_min_version 5.0.0
Summary:	Pulls APC data via APC UPS Daemon (apcupsd) for non-SNMP hardware
Name:		cacti-template-%{template}
Version:	1.1
Release:	8
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/usertemplate:data:apc:apcupsd:apcupsd_%{version}.zip
# Source0-md5:	eedc80bd5d93826b7df914f5070bf625
Patch0:		path.patch
URL:		http://docs.cacti.net/usertemplate:data:apc:apcupsd
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.554
BuildRequires:	unzip
Requires:	apcupsd
Requires:	cacti >= 0.8.7e-8
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts

%description
Pulls APC data via APC UPS Daemon (apcupsd) for non-SNMP hardware.

%prep
%setup -qc
%undos -f php
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{scriptsdir}}
cp -p *.xml $RPM_BUILD_ROOT%{resourcedir}
install -p *.php $RPM_BUILD_ROOT%{scriptsdir}

%post
%cacti_import_template %{resourcedir}/cacti_graph_template_apc_battery_statistics.xml
%cacti_import_template %{resourcedir}/cacti_graph_template_apc_line_statistics.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{scriptsdir}/query_apcupsd.php
%{resourcedir}/cacti_graph_template_apc_battery_statistics.xml
%{resourcedir}/cacti_graph_template_apc_line_statistics.xml
