%define name compiz-fusion
%define version 2010.0
%define release %mkrel 3

Summary: Compiz Fusion OpenGL compositing manager
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}
Source1: %{name}.defaults
License: GPL
Group: System/X11
URL: http://www.compiz-fusion.org/
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
Requires: compiz libcompizconfig ccsm compiz-fusion-plugins-main

%description
Compiz Fusion is a set of applications based on the compiz OpenGL
compositing manager.
It uses the ccp configuration backend, contains additional compiz
plugins, and provides the ccsm configuration interface.

This package provides some helper scripts and contains the necessary
dependancies to pull in the relevent required packages.

%prep
%setup -q -T -c

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m755 %{SOURCE0} %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/compositing-wm
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/compositing-wm

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/compositing-wm/%{name}.defaults


%changelog
* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.0-3mdv2011.0
+ Revision: 603845
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2010.0-2mdv2010.1
+ Revision: 522391
- rebuilt for 2010.1

* Thu Oct 15 2009 Colin Guthrie <cguthrie@mandriva.org> 2010.0-1mdv2010.0
+ Revision: 457731
- New version: 2010.0

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.0-4mdv2010.0
+ Revision: 423679
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2009.0-3mdv2010.0
+ Revision: 413262
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2009.0-2mdv2009.1
+ Revision: 350732
- rebuild

* Fri Sep 12 2008 Colin Guthrie <cguthrie@mandriva.org> 2009.0-1mdv2009.0
+ Revision: 284296
- Update version for 2009.0

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 2008.1-3mdv2009.0
+ Revision: 220508
- rebuild

* Mon Mar 10 2008 Colin Guthrie <cguthrie@mandriva.org> 2008.1-2mdv2008.1
+ Revision: 183388
- Revert r177015 and disable use of compiz-manager for now.

* Sat Mar 01 2008 Colin Guthrie <cguthrie@mandriva.org> 2008.1-1mdv2008.1
+ Revision: 177016
- Use compiz-manager script to start compiz

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.0.1-0.3mdv2008.1
+ Revision: 136331
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 03 2007 Colin Guthrie <cguthrie@mandriva.org> 0.0.1-0.3mdv2008.0
+ Revision: 95027
- Updated defaults now that compiz starts the decorator itself.
- Add BuildRoot (seems to be required for 2007.1 backport)

* Wed Aug 08 2007 Olivier Blin <oblin@mandriva.com> 0.0.1-0.2mdv2008.0
+ Revision: 60023
- exec compiz instead of keeping a spurious shell process (thanks to coling)

* Wed Aug 08 2007 Olivier Blin <oblin@mandriva.com> 0.0.1-0.1mdv2008.0
+ Revision: 60015
- initial compiz-fusion package
- Create compiz-fusion

