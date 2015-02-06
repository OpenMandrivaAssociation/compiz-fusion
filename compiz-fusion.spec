Name:		compiz-fusion
Version:	2012.1
Release:	5
Summary:	Compiz Fusion OpenGL compositing manager
License:	GPLv2
Group:		System/X11
URL:		http://www.compiz.org/
Source0:	%{name}
Source1:	%{name}.defaults
Requires:	compiz0.8
Requires:	ccsm0.8
Requires:	compiz-fusion-plugins-main
Conflicts:	compiz > 0.9
BuildArch:	noarch

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
install -d %{buildroot}%{_bindir}
install -m755 %{SOURCE0} %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/compositing-wm
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/compositing-wm

%files
%{_bindir}/%{name}
%{_datadir}/compositing-wm/%{name}.defaults

