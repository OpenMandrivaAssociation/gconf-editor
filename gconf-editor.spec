Summary:	An editor for the GConf configuration system
Name:		gconf-editor
Version:	2.32.0
Release:	5
#gw the COPYING is v3 but all comments say v2+
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	intltool
BuildRequires:	rarian
BuildRequires:	desktop-file-utils
BuildRequires:	libxslt-proc

%description
gconf-edit is an editor for the GConf configuration system

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

rm -rf %{buildroot}/var/lib/scrollkeeper

desktop-file-install --vendor="" \
  --remove-category="System" \
  --add-category="Settings" \
  --add-category="X-MandrivaLinux-System-Configuration-GNOME-Advanced" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome

%preun
%preun_uninstall_gconf_schemas %{name}

%files -f %{name}.lang
%doc README AUTHORS NEWS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/%{name}.schemas


%changelog
* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 2.32.0-3mdv2011.0
+ Revision: 677071
- rebuild to add gconf2 as req

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 2.32.0-2
+ Revision: 658389
- tighten br

* Mon Sep 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581420
- update to new version 2.32.0

* Thu Aug 05 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 566131
- new version
- update deps

* Tue Mar 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 529681
- update to new version 2.30.0

* Thu Mar 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 517940
- update to new version 2.29.92

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446599
- update to new version 2.28.0

* Mon Aug 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 420290
- update to new version 2.27.91

* Tue Mar 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356680
- update to new version 2.26.0

* Mon Feb 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 340937
- fix build deps
- update to new version 2.25.91

* Sun Oct 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295424
- new version

* Wed Sep 24 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0.1-1mdv2009.0
+ Revision: 287702
- new version

* Tue Sep 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287360
- new version

* Sun Aug 31 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 277786
- new version
- drop patch
- update file list
- update build deps
- update license

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 2.22.0-1mdv2009.0
+ Revision: 218423
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Mar 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 185037
- new version

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2.20.0-3mdv2008.1
+ Revision: 178724
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Sep 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89462
- new version

* Tue Sep 11 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.92-1mdv2008.0
+ Revision: 84447
- Remove old menu file
- Fix category in .desktop file to only display entry in Preferences/Advanced GNOME menu

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - new version
    - fix icon in desktop file

* Mon Aug 27 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 71885
- new version


* Tue Mar 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 142144
- new version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - no need to package big ChangeLog when NEWS is already there

* Mon Dec 18 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.0-1mdv2007.1
+ Revision: 98385
- mkrel
- Import gconf-editor

* Mon Dec 18 2006 Götz Waschk <waschk@mandriva.org> 2.17.0-1
- add omf files
- New version 2.17.0

* Wed Sep 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- New version 2.16.0

* Tue Aug 15 2006 Götz Waschk <waschk@mandriva.org> 2.15.92-1mdv2007.0
- add scrollkeeper stuff
- New release 2.15.92

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 2.15.91-2mdv2007.0
- fix buildrequires

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 2.15.91-1mdv2007.0
- drop patch
- New release 2.15.91

* Thu Aug 03 2006 Götz Waschk <waschk@mandriva.org> 2.14.0-3mdv2007.0
- spec fixes
- xdg menu

* Sat Apr 29 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.0-2mdk
- Patch0 (CVS): fix crash when changing value (found by pterjan)

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-2mdk
- Use mkrel

* Wed Nov 30 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-1mdk
- New release 2.12.1

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-1mdk
- Release 2.12.0

* Fri Aug 19 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.0-3mdk 
- Fix icon path

* Thu May 26 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.0-2mdk 
- run gtk-update-icon-cache at post/postun

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.0-1mdk 
- Release 2.10.0 (based on Götz Waschk package)
- don't uninstall schema on upgrade

* Wed Jan 05 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.2-4mdk 
- Rebuild with latest howl

* Mon Nov 15 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.8.2-3mdk
- add BuildRequires: scrollkeeper

* Fri Nov 12 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.2-2mdk
- fix buildrequires

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.2-1mdk
- add schema and omf files
- requires new gconf
- New release 2.8.2

* Tue Jun 15 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- reenable libtoolize
- New release 2.6.2

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.1-2mdk
- Fix BuildRequires

* Sat Apr 17 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- new version

* Wed Apr 07 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-1mdk
- Release 2.6.0 (with Götz help)
- Remove patch0 (merged upstream)

