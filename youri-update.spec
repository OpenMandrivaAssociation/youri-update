%define name	youri-update
%define version 0.1.1
%define release 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Youri update tool
License:	GPL or Artistic
Group:		Development/Other
Source:		http://youri.zarb.or/download/%{name}-%{version}.tar.bz2
Url:		https://youri.zarb.org
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

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


%changelog
* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 0.1.1-5mdv2011.0
+ Revision: 556499
- rebuild for new perl

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.1.1-4mdv2010.0
+ Revision: 435374
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.1.1-3mdv2009.0
+ Revision: 243002
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2008.0
+ Revision: 20752
- Import youri-update



* Wed May 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2008.0
- first mdv release
