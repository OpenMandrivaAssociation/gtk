%define major		1.2
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	The GIMP ToolKit (GTK+), a library for creating GUIs for X
Name:		gtk+
Version:	1.2.10
Release:	56
License:	LGPL
Group:		System/Libraries
Source0:	ftp://ftp.gimp.org/pub/gtk/v1.2/gtk+-%{version}.tar.bz2
Source1:	gtk+-1.2.10-vi.po.bz2
# (fc) 1.2.10-2mdk ximian patch changing drawing when no shadow is set for menubar
Patch2:		gtkmenubar-noborder.patch
# (pablo) better gtkrc definitions
Patch3:		gtk+-1.2.10-gtkrc_files.patch
# (fc) 1.2.10-8mdk GNOME CVS patch correcting bad focus (seen in Evolution and gnomecc)
Patch4:		gtk+-1.2.10-focus.patch
# (pablo) load locale based gtkrc (GNOME CVS)
Patch5:		gtk+-1.2.10-rclocale.patch
# (fc) 1.2.10-10mdk fix alignement warning on ia64 (Rawhide)
Patch6:		gtk+-1.2.10-alignment.patch
# (fc) 1.2.10-10mdk Improve exposure compression (GNOME CVS)
Patch7:		gtk+-1.2.10-expose.patch
# (fc) 1.2.10-10mdk Don't screw up CTEXT encoding for UTF-8 (Rawhide)
Patch8:		gtk+-1.2.10-ctext.patch
# (fc) 1.2.10-10mdk Accept KP_Enter as a synonym for Return everywhere (Rawhide)
Patch9:		gtk+-1.2.10-kpenter.patch
# (fc) 1.2.10-10mdk Allow theme switching to work properly when no windows are realized (Rawhide)
Patch10:	gtk+-1.2.10-themeswitch.patch
# (fc) 1.2.10-10mdk Fix crash when switching themes (Rawhide)
Patch11:	gtk+-1.2.10-pixmapref.patch
# (fc) 1.2.10-10mdk Fix computation of width of missing characters (Rawhide)
Patch12:	gtk+-1.2.10-missingchar.patch
# (fc) 1.2.10-20mdk set _NET_WM_PID on gdkwindow (GNOME CVS)
Patch15:	gtk+-1.2.10-netwmpid.patch
# (fc) 1.2.10-22mdk fix Fix check of wrong variable on gtklabel (GNOME CVS)
Patch16:	gtk+-1.2.10-labelvariable.patch
# (fc) 1.2.10-22mdk fix GtkCombo occasionally segfaults after content is changed and list shown (GNOME CVS) Bugzilla 58024
Patch17:	gtk+-1.2.10-gtklist.patch
# (fc) 1.2.10-22mdk option menu doesn't appear centered when applied a border (GNOME CVS) Bugzilla 54585
Patch18:	gtk+-1.2.10-border.patch
# (fc) 1.2.10-22mdk DnD code doesn't notice new windows (GNOME CVS) Bugzilla 56349
Patch19:	gtk+-1.2.10-dndnewwindow.patch
# (fc) 1.2.10-26mdk don't set -L/usr/lib in gtk-config
Patch20:	gtk+-1.2.10-libdir.patch
# (fc) 1.2.10-27mdk Fix file selection delete-dir when changing directory problem
# also, fix memory corruption problem when changing directories. (Rawhide)
Patch21:	gtk+-1.2.10-deletedir.patch 
# fc) 1.2.10-27mdk Improve warning for missing fonts (Rawhide)
Patch22:	gtk+-1.2.10-fontwarning.patch
# (fc) 1.2.10-27mdk Allow themes to make scrollbar trough always repaint (rawhide)
Patch23:	gtk+-1.2.10-troughpaint.patch
# (fc) 1.2.10-28mdk Fix a crash that can happen in some apps when the current
# locale is not supported by XLib. (rawhide)
Patch24:	gtk+-1.2.10-localecrash.patch
# (fc) 1.2.10-29mdk fix loop and crash in file selector when / is not readable (bug #90)
Patch25:	gtk+-1.2.10-fileselectorfallback.patch
# (fc) 1.2.10-30mdk change default colors to match GTK2 2.2 colors
Patch26:	gtk+-1.2.10-defaultcolor.patch
Patch27:	gtk+-1.2.10-fix-underquoted-calls.patch
# (fc) 1.2.10-45mdv ugly hack to skip argb visuals
Patch28:	gtk+-1.2.10-argb.patch
# (from fedora)
Patch29:	gtk+-1.2.10-gtkgdkdep.patch

URL:		http://www.gtk.org
BuildRequires:	autoconf2.1
BuildRequires:	automake1.4
BuildRequires:	libtool
BuildRequires:	pkgconfig(glib)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xext)

%description
The gtk+ package contains the GIMP ToolKit (GTK+), a library for creating
graphical user interfaces for the X Window System.  GTK+ was originally
written for the GIMP (GNU Image Manipulation Program) image processing
program, but is now used by several other programs as well. This is GTK+ 
1.2, a legacy version. The current version is GTK+ 2.

%package common
Summary:	Common data for gtk+ library
Group:		System/Libraries
Conflicts:	%{libname} < 1.2.10-56

%description common
Common data for gtk+ library.

%package -n	%{libname}
Summary:	Main library for gtk+
Group:		System/Libraries
Provides:	gtk+ = %{version}-%{release}
Requires:	%{name}-common >= %{version}
Suggests:	galaxy-gtk12

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with gtk+.

%package -n	%{develname}
Summary:	Development tools for GTK+ (GIMP ToolKit) applications
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}-%{release}
Requires:	%{name}-common >= %{version}
Provides:	gtk-devel = %{version}-%{release}
Provides:	gtk+-devel = %{version}-%{release}
Provides:	libgtk+-devel = %{version}-%{release}
Provides:	gtk+%{major}-devel = %{version}-%{release}

%description -n	%{develname}
The libgtk+1.2-devel package contains the static libraries and header files
needed for developing GTK+ (GIMP ToolKit) applications. The %{develname}
package contains GDK (the General Drawing Kit, which simplifies the interface
for writing GTK+ widgets and using GTK+ widgets in applications), and GTK+
(the widget set). Install %{develname} if you need to develop GTK+ 
applications. This is GTK+ 1.2, a legacy version. The current version is
GTK+ 2.

%prep
%setup -q
%patch2 -p1 -b .noshadow
%patch3 -p1 -b .gtkrc
%patch4 -p1 -b .focus
%patch5 -p1 -b .rclocale
%patch6 -p1 -b .ia64
%patch7 -p1 -b .expose
%patch8 -p1 -b .ctext
%patch9 -p1 -b .kpenter
%patch10 -p1 -b .themeswitch
%patch11 -p1 -b .pixmapref
%patch12 -p1 -b .missingchar
%patch15 -p1 -b .netwmpid
%patch16 -p1 -b .labelvariable
%patch17 -p1 -b .gtklist
%patch18 -p1 -b .border
%patch19 -p1 -b .dndnewwindow
%patch20 -p1 -b .libdir
%patch21 -p1 -b .deletedir
%patch22 -p1 -b .fontwarning
%patch23 -p1 -b .troughpaint
%patch24 -p1 -b .localecrash
%patch25 -p1 -b .fileselectorfallback
%patch26 -p1 -b .defaultcolor
%patch27 -p1 -b .underquoted
%patch28 -p1 -b .argb
%patch29 -p1 -b .gdkdep

# vi.po is not encoded in utf-8
bzcat %{SOURCE1} > po/vi.po

libtoolize --install --force
# needed by patch 3, 29
# it doesn't work with 2.5. I tested. -AdamW 2007/07
autoreconf-2.13

%build
%define Werror_cflags %nil
%configure  --with-xinput=xfree --with-native-locale
%make LIBTOOL="%{_bindir}/libtool --tag=CC"

make check

%install
%makeinstall_std LIBTOOL=%{_bindir}/libtool

# create a default theme file
cat << EOF > %{buildroot}%{_sysconfdir}/gtk/gtkrc
include "/usr/share/themes/Galaxy/gtk/gtkrc"
EOF

%multiarch_binaries %{buildroot}%{_bindir}/*

%find_lang %{name}

%files common -f %{name}.lang
%{_datadir}/themes
%dir %{_sysconfdir}/gtk
%config(noreplace) %{_sysconfdir}/gtk/*

%files -n %{libname}
%{_libdir}/lib*.so.*

%files -n %{develname}
%doc docs/*.txt AUTHORS ChangeLog NEWS* README* TODO docs/html
%{_libdir}/lib*.so
%{_mandir}/man1/*
%{_infodir}/g?k.info*
%{_includedir}/*
%{_datadir}/aclocal/*
%{multiarch_bindir}/*

%{_bindir}/gtk-config
%{_libdir}/pkgconfig/*


%changelog
* Wed Jun 13 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2.10-54
+ Revision: 805314
- Drop some legacy junk

* Tue Feb 21 2012 Jon Dill <dillj@mandriva.org> 1.2.10-53
+ Revision: 778789
- rebuild for libffi4

* Mon Dec 05 2011 Götz Waschk <waschk@mandriva.org> 1.2.10-52
+ Revision: 737733
- adapt for multiarch breakage in rpm5
- spec cleanup
- rebuild

* Wed Dec 23 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.10-51mdv2011.0
+ Revision: 481672
- remove patch added to wrong package
- add upstream patch to fix sylpheed crash

* Thu Dec 03 2009 Götz Waschk <waschk@mandriva.org> 1.2.10-51mdv2010.1
+ Revision: 472805
- call libtoolize
- disable Werror

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Anssi Hannula <anssi@mandriva.org>
    - rediff patch gtkrc_files.patch

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.2.10-50mdv2009.0
+ Revision: 264643
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon May 26 2008 Anssi Hannula <anssi@mandriva.org> 1.2.10-49mdv2009.0
+ Revision: 211355
- buildrequires automake1.4 for autoreconf-2.13 with gtkgdkdep.patch

  + Pixel <pixel@mandriva.com>
    - Add a dependency on libgdk to libgtk (from fedora, rhbz#106677)

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.2.10-48mdv2008.1
+ Revision: 150244
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Sep 13 2007 Frederic Crozat <fcrozat@mandriva.com> 1.2.10-47mdv2008.0
+ Revision: 85153
- Add default theme as Galaxy in /etc/gtk/gtkrc and add a suggests for it

  + Thierry Vignaud <tv@mandriva.org>
    - kill file require on info-install

* Sat Jul 21 2007 Adam Williamson <awilliamson@mandriva.org> 1.2.10-46mdv2008.0
+ Revision: 54343
- rebuild for 2008
- new devel policy
- bunzip2 patches
- minor spec clean
- Import gtk+



* Tue Jul 25 2006 Frederic Crozat <fcrozat@mandriva.com> 1.2.10-45mdv2007.0
- Patch28: prevent crash when composite is enabled

* Wed Jan 25 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.10-44mdk
- fix underquoted calls (P27)
- %%mkrel
- cosmetics

* Wed Jan 11 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.2.10-43mdk
- add BuildRequires: libtool

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.2.10-42mdk
- Rebuild

* Tue Feb 01 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-41mdk 
- multiarch
- clean specfile

* Wed Aug 25 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.10-40mdk
- fixed gtkrc files for Thai, Vietnamlese and Azeri in UTF-8

* Mon Jun 21 2004 Stefan van der Eijk <stefan@mandrake.org> 1.2.10-39mdk
- BuildRequires

* Thu Feb 26 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-38mdk
- Fix dislint error

* Thu Jul 31 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.2.10-37mdk
- Provides: gtk+1.2-devel

* Thu Jul 31 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.2.10-36mdk
- use system libtool, mklibname since maintainer failed to do so

* Fri Jul 18 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.2.10-35mdk
- rebuild to get rid of oden's signature (should'nt sign packages with our own keys!)

* Thu Jul 10 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.2.10-34mdk
- rebuild to obtain automatic devel provides

* Tue May 20 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.10-33mdk
- rebuild to obtain automatic devel provides

* Mon Mar 10 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.10-32mdk
- added missing gtkrc files for zh_HK and zh_SG

* Wed Mar 05 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.10-31mdk
- improved various gtkrc files to have better fonts in utf-8 mode
  for old gtk1 programs

* Wed Jan 22 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-30mdk
- Patch26: use same default colors as GTK+ 2.2
- Use utf-8 encoded vietnamese po file

* Wed Sep 11 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-29mdk
- Patch25: fix infinit loop & crash in fileselector when / is not readable (bug #90)

* Mon Aug 26 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-28mdk
- Patch24 (Rawhide): Fix a crash that can happen in some apps when the current
  locale is not supported by XLib.

* Tue Jul 30 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-27mdk
- Build with --native-locale switch enabled
- Resync patch19 with CVS
- Patch21 (Rawhide): Fix file selection delete-dir when changing directory problem and also, fix memory corruption problem when changing directories
- Patch22 (Rawhide): Improve warning for missing fonts
- Patch23 (Rawhide): Allow themes to make scrollbar trough always repaint

* Mon Jun 17 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-26mdk
- Patch20: fix gtk-config to not give -L/usr/lib for --libs (Geoffrey Lee)

* Wed Feb 27 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.10-25mdk
- splitted rclocale patch into gtkrc one and rc reading one, and used
  a corrected patch for the later.

* Mon Feb 25 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-24mdk
- Removing patch 5 (Ximian based file selector patch) since it generates
  crashes with some applications

* Thu Feb 14 2002 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.10-23mdk
- integrated latest Basque translations (and others, from Gnome CVS)
- added and improved gtkrc files for utf-8 locales

* Wed Feb 13 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-22mdk
- Patch16 (GNOME CVS): fix check on wrong variable in gtk_label
- Patch17 (GNOME CVS): fix occasionnal GtkList segfault (bug 58024)
- Patch18 (GNOME CVS): option menu doesn't appear centered when applied a border (bug 54585)
- Patch19 (GNOME CVS): DnD code doesn't notice new windows (bug 56349)
- Regenerate patch 5 with latest version of Ximian patch
- Regenerate patches 3 & 7 to use official fixes from GNOME CVS

* Wed Jan 23 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.10-21mdk
- In the never-ending search for the best fontsets, change the gtkrc of
  Chinese, Korean, and Japanese yet again, to define the best fonts, and
  also to make Mozilla look nice with scalable X fonts :)
- Clear up the long commented AndrewLee big5 hack way back from 1.2.8-6mdk.

* Tue Jan 22 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-20mdk
- Patch15: set _NET_WM_PID on gdkwindow (GNOME CVS)
- Remove patches 13 & 14 (versionned files), since new GTK+2 has been
versionned by authors to no longer conflict with GTK+ 1.2

* Sun Jan 13 2002 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.10-19mdk
- gtk+-rclocale.patch:
  - Back to font size 14 for Japanese fonts.

* Wed Oct 24 2001 DindinX <odin@mandrakesoft.com> 1.2.10-18mdk
- Grr. *really* versionned gtkrc (pointed out by Pixel)

* Tue Oct 23 2001 DindinX <odin@mandrakesoft.com> 1.2.10-17mdk
- versionned gtkrc...

* Mon Oct 09 2001 DindinX <odin@mandrakesoft.com> 1.2.10-16mdk
- resurect the mo files

* Fri Oct 05 2001 DindinX <odin@mandrakesoft.com> 1.2.10-15mdk
- versioned i18n

* Sun Sep 16 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.10-14mdk
- added gtkrc file for utf-8 georgian and fixed Thai and Russian ones

* Sun Sep 16 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.10-13mdk
- fixed CJK fontsets in gtkrc files

* Fri Sep 14 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.10-12mdk
- rebuild including latest translations
- added some more gtkrc files (utf-8 and improvec cjk ones)

* Fri Aug 31 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-11mdk
- Remove /etc/gtk/gtkrc : offical gtk doesn't provide any default one and
  previous "default" gtkrc was still breaking some themes on tooltips

* Thu Aug 30 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-10mdk
- /etc/gtk/gtkrc is back (and use default gtkrc)
- Patch5: add navigation button to file selector (from Ximian)
- Merge patches from Rawhide :
 - Patch6:  patch for alignment warnings on ia64
 - Patch7:  patch to vastly improve expose compression
 - Patch8:  not screw up CTEXT for UTF-8 locales
 - Patch9 : Accept KP_Enter as well as Return
 - Patch10: fix for theme switching in nautilus sidebar tabs 
  (and other similar situations)
 - Patch11: Fix refcounting problem in gtk_style_copy() that might affect 
   theme switching.
 - Patch12: Fix problem with width computation for missing characters

* Mon Jul 30 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-9mdk
- Fixes from Götz Waschk:
 - pkgconfig files
 - html doc

* Wed Jul 25 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-8mdk
- Patch4: fix focus problem with Evolution and Gnome control-center
- add version in provides

* Wed Jul 04 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 1.2.10-7mdk
- More specific %%_infodir file glob, to prevent file "dir" from
  being packaged. (occurs on alpha but not i586)

* Tue Jul 03 2001 Stefan van der Eijk <stefan@eijk.nu> 1.2.10-6mdk
- BuildRequires:	XFree86-devel

* Wed Jun 27 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.10-5mdk
- fixed some locale weirdness 

* Mon Jun 11 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.10-4mdk
- corrected a bug of my patch
- added gtkrc.utf-8 to the package

* Wed Jun 06 2001 Pablo Saratxaga <pablo@mandrakesoft.com> 1.2.10-3mdk
- removed various obsolete stuff
- added a charset-based selection of gtkrc files
- should now work in utf-8 locales!

* Fri May  4 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.2.10-2mdk
- Patch2 (ximian) : modify drawing when no shadow for menubar

* Mon Apr  2 2001 DindinX <odin@mandrakesoft.com> 1.2.10-1mdk
- 1.2.10

* Thu Mar 29 2001 David BAUDENS <baudens@mandrakesoft.com> 1.2.9-8mdk
- Requires mandrake_desk (use new theme)

* Tue Mar 27 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.9-7mdk
- Apply ctext patch from Abel Cheung <maddog@linuxhall.org>.

* Wed Mar 14 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 1.2.9-6mdk
- require common-licenses.
- clean up spec a tiny bit.
- more docs.
- fix rpmlint warnings.
- install info files the correct way.

* Mon Mar 05 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.9-5mdk
- Fix symlink.

* Mon Mar 05 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.9-4mdk
- More Chinese cleanups.

* Mon Mar 05 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.9-3mdk
- Cleanup of Chiense.

* Mon Mar  5 2001 DindinX <odin@mandrakesoft.com> 1.2.9-2mdk
- Grr, rebuild with glib-devel installed on the cluster

* Fri Mar  2 2001 DindinX <odin@mandrakesoft.com> 1.2.9-1mdk
- 1.2.9

* Tue Dec 19 2000 DindinX <odin@mandrakesoft.com> 1.2.8-11mdk
- use -j in tar instead of the (very) obsolete -I

* Tue Nov 28 2000 DindinX <odin@mandrakesoft.com> 1.2.8-10mdk
- add som obsoletes: tags
- use more macros
- fix description

* Mon Nov 27 2000 DindinX <odin@mandrakesoft.com> 1.2.8-9mdk
- Grr. Now really respect the new naming policy
- move some doc from libgtk+1.2 to libgtk+1.2-devel

* Mon Nov 27 2000 DindinX <odin@mandrakesoft.com> 1.2.8-8mdk
- new naming policy
- temporary removed the submenu-navigation patch, since xmms has some issue
  with it (imho xmms should be fixed...).

* Fri Nov 03 2000 DindinX <odin@mandrakesoft.com> 1.2.8-7mdk
- rebuild with gcc-2.96

* Thu Oct 26 2000 DindinX <odin@mandrakesoft.com> 1.2.8-6mdk
- Solve show Big5(temporality) (from Andrew Lee <andrew@cle.linux.org.tw>)

* Tue Oct 24 2000 DindinX <odin@mandrakesoft.com> 1.2.8-5mdk
- Backported the submenu-navigation patch
- Added many docs to gtk+-devel

* Mon Aug 28 2000 DindinX <odin@mandrakesoft.com> 1.2.8-4mdk
- remove --enable-debug=no since some programs segfault because of this
  (reported by Frederic Crozat)

* Fri Aug 25 2000 DindinX <odin@mandrakesoft.com> 1.2.8-3mdk
- use %%lang and %%make
- add the noreplace flag for %%config

* Tue Aug 01 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2.8-2mdk
- rebuild with macros
- rebuild for BM
- misc fixes

* Wed Jun 7 2000 DindinX <odin@mandrakesoft.com> 1.2.8-1mdk
- 1.2.8

* Tue Mar 21 2000 DindinX <odin@mandrakesoft.com> 1.2.7-4mdk
- corrected the paths in glib-config

* Tue Mar 21 2000 DindinX <odin@mandrakesoft.com> 1.2.7-3mdk
- Patches cleanups (now use 1.2.7 from www.gtk.org instead of 1.2.4 + patches

* Mon Mar 20 2000 DindinX <odin@mandrakesoft.com> 1.2.7-2mdk
- Group and spec fixes

* Sat Feb 19 2000 DindinX <odin@mandrakesoft.com> 1.2.7-1mdk
- 1.2.7

* Thu Jan 27 2000 DindinX <odin@mandrakesoft.com> 1.2.6-8mdk

- disable all debugging stuff by adding --enable-debug=no to the configure
  script.

* Thu Jan 20 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2.6-7mdk

- enabled XInput support

* Thu Jan  6 2000 Pixel <pixel@mandrakesoft.com>
- more stars in the fontset of et of vi_VN.tcvn

* Thu Jan  6 2000 Pixel <pixel@mandrakesoft.com>
- really 1.2.6 (and silimi)

* Fri Nov 05 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- New po files from Pablo
- Remove summary/description clutter 

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Enable SMP build/check
- 1.2.6

* Wed Sep 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Real 1.2.5 (chmou sux).
- 1.2.5

* Tue Aug 31 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- a little i18n patch for gfontsel
- latest translations
- tooltip colours in /etc/gtkrc

* Thu Aug 26 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.2.4

* Tue Aug 24 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove completely the /etc/gtk/gtkrc (completely sucks :-(( )

* Sat Aug 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove style "default-text" in gtkrc (cause trouble with i18n language).

* Fri Jul 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Rebuild without glib-1.3 :-((

* Wed Jul 14 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- included latest *.po files from GNOME CVS
- and added back descriptions from RH 5.2
- added an icon for the rpm

* Thu Jul 08 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- put back --sysconfdir=/etc for config time (otherwise the files on /etc are
  never read)

* Mon Jun 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build for new environment.

* Thu May 12 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 1.2.3

* Fri Apr 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adpatations.

* Thu Apr 01 1999 Michael Fulbright <drmike@redhat.com>
- patches from owen to handle various gdk bugs

* Sun Mar 28 1999 Michael Fulbright <drmike@redhat.com>
- added XFree86-devel requirement for gtk+-devel

* Thu Mar 25 1999 Michael Fulbright <drmike@redhat.com>
- version 1.2.1

* Wed Mar 17 1999 Michael Fulbright <drmike@redhat.com>
- removed /usr/info/dir.gz file from package

* Fri Feb 26 1999 Michael Fulbright <drmike@redhat.com>
- Version 1.2.0

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- version 1.2.0pre2, patched to use --sysconfdir=/etc

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- patched in Owen's patch to fix Metal theme

* Fri Feb 05 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.15

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.14

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.13

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.12

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- added Theme directory to file list
- up to 1.1.7 for GNOME freeze

* Sun Oct 25 1998 Shawn T. Amundson <amundson@gtk.org>
- Fixed Source: to point to v1.1 

* Tue Aug 04 1998 Michael Fulbright <msf@redhat.com>
- change %%postun to %%preun

* Mon Jun 27 1998 Shawn T. Amundson
- Changed version to 1.1.0

* Thu Jun 11 1998 Dick Porter <dick@cymru.net>
- Removed glib, since it is its own module now

* Mon Apr 13 1998 Marc Ewing <marc@redhat.com>
- Split out glib package

* Tue Apr  8 1998 Shawn T. Amundson <amundson@gtk.org>
- Changed version to 1.0.0

* Tue Apr  7 1998 Owen Taylor <otaylor@gtk.org>
- Changed version to 0.99.10

* Thu Mar 19 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.9
- Changed gtk home page to www.gtk.org

* Thu Mar 19 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.8

* Sun Mar 15 1998 Marc Ewing <marc@redhat.com>
- Added aclocal and bin stuff to file list.
- Added -k to the SMP make line.
- Added lib/glib to file list.

* Fri Mar 14 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.7

* Fri Mar 14 1998 Shawn T. Amundson <amundson@gimp.org>
- Updated ftp url and changed version to 0.99.6

* Thu Mar 12 1998 Marc Ewing <marc@redhat.com>
- Reworked to integrate into gtk+ source tree
- Truncated ChangeLog.  Previous Authors:
  Trond Eivind Glomsrod <teg@pvv.ntnu.no>
  Michael K. Johnson <johnsonm@redhat.com>
  Otto Hammersmith <otto@redhat.com>
