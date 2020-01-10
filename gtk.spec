%define api	1.2
%define major	0
%define libgtk	%mklibname gtk %{api} %{major}
%define libgdk	%mklibname gdk %{api} %{major}
%define devname	%mklibname %{name} -d
%define _disable_lto 1

Summary:	The GIMP ToolKit (GTK+), a library for creating GUIs for X
Name:		gtk+
Version:	1.2.10
Release:	59
License:	LGPLv2
Group:		System/Libraries
Url:		http://www.gtk.org
Source0:	http://download.gimp.org/pub/gtk/v1.2/%{name}-%{version}.tar.gz
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
Provides:	gtk+ = %{version}-%{release}
Suggests:	galaxy-gtk12
Conflicts:	%{_lib}gtk+1.2 < 1.2.10-56

%description common
Common data for gtk+ library.

%package -n	%{libgtk}
Summary:	Main library for gtk+
Group:		System/Libraries
Suggests:	%{name}-common >= %{version}
Obsoletes:	%{_lib}gtk+1.2 < 1.2.10-57

%description -n	%{libgtk}
This package contains the library needed to run programs dynamically
linked with gtk+.

%package -n	%{libgdk}
Summary:	Main library for gtk+
Group:		System/Libraries
Suggests:	%{name}-common >= %{version}
Obsoletes:	%{_lib}gtk+1.2 < 1.2.10-57

%description -n	%{libgdk}
This package contains the library needed to run programs dynamically
linked with gtk+.

%package -n	%{devname}
Summary:	Development tools for GTK+ (GIMP ToolKit) applications
Group:		Development/GNOME and GTK+
Requires:	%{libgtk} = %{version}-%{release}
Requires:	%{libgdk} = %{version}-%{release}
Requires:	%{name}-common >= %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
The libgtk+1.2-devel package contains the static libraries and header files
needed for developing GTK+ (GIMP ToolKit) applications. The %{devname}
package contains GDK (the General Drawing Kit, which simplifies the interface
for writing GTK+ widgets and using GTK+ widgets in applications), and GTK+
(the widget set). Install %{devname} if you need to develop GTK+ 
applications. This is GTK+ 1.2, a legacy version. The current version is
GTK+ 2.

%prep
%setup -q
%autopatch -p1

# vi.po is not encoded in utf-8
bzcat %{SOURCE1} > po/vi.po

libtoolize --install --force
# needed by patch 3, 29
# it doesn't work with 2.5. I tested. -AdamW 2007/07
autoreconf-2.13

%build
%define Werror_cflags %{nil}
%configure \
	--with-xinput=xfree \
	--with-native-locale

%make LIBTOOL="%{_bindir}/libtool --tag=CC"

%check
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
%dir %{_sysconfdir}/gtk
%config(noreplace) %{_sysconfdir}/gtk/*
%{_datadir}/themes

%files -n %{libgtk}
%{_libdir}/libgtk-%{api}.so.%{major}*

%files -n %{libgdk}
%{_libdir}/libgdk-%{api}.so.%{major}*

%files -n %{devname}
%doc docs/*.txt AUTHORS ChangeLog NEWS* README* TODO docs/html
%{_bindir}/gtk-config
%{multiarch_bindir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%{_mandir}/man1/*
%{_infodir}/g?k.info*
%{_includedir}/*
