%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	An editor for the GConf configuration system
Name:		gconf-editor
Version:	3.0.1
Release:	1
#gw the COPYING is v3 but all comments say v2+
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://www.gnome.org/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gconf-editor/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	rarian
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gnome-doc-utils)

%description
gconf-edit is an editor for the GConf configuration system

%prep
%setup -q

%build
%configure

%make

%install
%makeinstall_std

rm -rf %{buildroot}/var/lib/scrollkeeper

desktop-file-install --vendor="" \
	--remove-category="System" \
	--add-category="Settings" \
	--add-category="X-MandrivaLinux-System-Configuration-GNOME-Advanced" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%doc README AUTHORS NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/%{name}.schemas

