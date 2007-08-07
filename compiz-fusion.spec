%define name compiz-fusion
%define version 0.0.1
%define release %mkrel 0.1

Summary: Compiz Fusion OpenGL composing manager
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}
Source1: %{name}.defaults
License: GPL
Group: System/X11
URL: http://www.compiz-fusion.org/
BuildArch: noarch
Requires: compiz libcompizconfig ccsm compiz-fusion-plugins-main

%description
Compiz Fusion is a set of applications based on the compiz OpenGL
compositing manager.
It uses the ccp configuration backend, contains additional compiz
plugins, and provides the ccsm configuration interface.

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
