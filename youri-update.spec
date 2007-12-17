%define name	youri-update
%define version 0.1.1
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Youri update tool
License:	GPL or Artistic
Group:		Development/Other
Source:		http://youri.zarb.or/download/%{name}-%{version}.tar.bz2
Url:		http://youri.zarb.org
BuildArch:	    noarch

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

youri-update allows to update packages. When given an explicit new version, it
downloads new sources automatically, updates the spec file and builds a new
version. When not given a new version, it just updates the spec file a builds a
new release.

It is a rewrite of rpmbuildupdate, using a configuration files and command line
options more consistent with other youri tools.

%prep
%setup -q

%build
%configure2_5x
%make

%check
%__make check

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README
%config(noreplace) %{_sysconfdir}/youri
%{_bindir}/youri-update
%{_mandir}/man1/*
