%define name nuapplet
%define version 0.7
%define release %mkrel 1

Summary: NuFW applet for the GNOME panel
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://software.inl.fr/releases/Nuapplet/%{name}-%{version}.tar.bz2
License: GPL
Group: Monitoring
Url: http://software.inl.fr/releases/Nuapplet/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gnome-panel-devel
BuildRequires: libeel-devel
BuildRequires: scrollkeeper
BuildRequires: perl-XML-Parser
BuildRequires: libnuclient-devel
Requires: libnuclient

%description
NuApplet is a graphical client for NuFW. It is a GNOME 2.x applet 
that uses the client authentication library of the NuFW project. 

It is a user-friendly alternative to the console client, nutcpc. 

It supports multiple languages thanks to gettext.

%prep
%setup -q

sh autogen.sh

%build
%configure2_5x
make

%install
rm -rf %buildroot
%makeinstall

%find_lang %name

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README 
%{_bindir}/%{name}
%{_datadir}/gnome-2.0/ui/NuFWContextMenu.xml
%{_datadir}/pixmaps/*.svg
%{_libdir}/bonobo/servers/NuApplet.server
