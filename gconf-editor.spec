Summary: An editor for the GConf configuration system
Name: gconf-editor
Version: 2.26.0
Release: %mkrel 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
#gw the COPYING is v3 but all comments say v2+
License: GPLv2+
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libgnomeui2-devel
BuildRequires: libGConf2-devel >= 2.9.2
BuildRequires: polkit-devel
BuildRequires: intltool
BuildRequires: desktop-file-utils
BuildRequires: gnome-doc-utils libxslt-proc
Requires(post): scrollkeeper
Requires(postun): scrollkeeper
URL: http://www.gnome.org/

%description
gconf-edit is an editor for the GConf configuration system

%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

rm -rf $RPM_BUILD_ROOT/var/lib/scrollkeeper

desktop-file-install --vendor="" \
  --remove-category="System" \
  --add-category="Settings" \
  --add-category="X-MandrivaLinux-System-Configuration-GNOME-Advanced" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{name} --with-gnome
for omf in %buildroot%_datadir/omf/%name/%name-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/%name-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%post_install_gconf_schemas %name
%update_icon_cache hicolor
%update_scrollkeeper
%endif

%preun
%preun_uninstall_gconf_schemas %name

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%clean_scrollkeeper
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/*/*
%_datadir/%name
%_sysconfdir/gconf/schemas/%name.schemas
%dir %_datadir/omf/%name
%_datadir/omf/%name/*-C.omf


