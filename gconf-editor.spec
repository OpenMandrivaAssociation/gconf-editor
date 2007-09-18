Summary: An editor for the GConf configuration system
Name: gconf-editor
Version: 2.20.0
Release: %mkrel 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch: gconf-editor-2.19.92-desktopentry.patch
License: GPL
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libgnomeui2-devel
BuildRequires: libGConf2-devel >= 2.9.2
BuildRequires: perl-XML-Parser
BuildRequires: desktop-file-utils
BuildRequires: gnome-doc-utils libxslt-proc
Requires(post): scrollkeeper
Requires(postun): scrollkeeper
URL: http://www.gnome.org/

%description
gconf-edit is an editor for the GConf configuration system

%prep
%setup -q
%patch -p1

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

%post
%{update_menus}
%post_install_gconf_schemas %name
%update_icon_cache hicolor
%update_scrollkeeper

%preun
%preun_uninstall_gconf_schemas %name

%postun
%{clean_menus}
%clean_icon_cache hicolor
%clean_scrollkeeper

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/48x48/apps/gconf-editor.png
%_sysconfdir/gconf/schemas/%name.schemas
%dir %_datadir/omf/%name
%_datadir/omf/%name/*-C.omf


