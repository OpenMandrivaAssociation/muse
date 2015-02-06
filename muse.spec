Name:          muse
Summary:       Midi/Audio Music Sequencer
Version:       2.0.1
Release:       2
License:       Public Domain and GPLv2 and GPLv2+ and LGPLv2+
Group:         Sound
URL:           http://www.muse-sequencer.org/
Source0:       https://downloads.sourceforge.net/project/lmuse/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires: libalsa-devel
BuildRequires: jackit-devel
BuildRequires: cmake
BuildRequires: dssi-devel
BuildRequires: fluidsynth-devel
BuildRequires: liblo-devel
BuildRequires: libsamplerate-devel
BuildRequires: sndfile-devel
BuildRequires: pkgconfig
BuildRequires: python-devel
BuildRequires: qt4-devel
BuildRequires: desktop-file-utils
BuildRequires: libuuid-devel

%description
MusE is a MIDI/Audio sequencer with recording and editing capabilities. It can
perform audio effects like chorus/flanger in real-time via LASH and it supports
Jack and ALSA interfaces. MusE aims to be a complete multitrack virtual studio 
for Linux.


%prep
%setup -q

%build
mkdir build
pushd build
cmake .. \
   -DMusE_DOC_DIR=%{_docdir}/%{name}-%{version}/ \
   -DENABLE_PYTHON=1 -DENABLE_LASH=0 -DENABLE_FLUID=0 \
   -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR:PATH=%_libdir

make

%install
pushd build
%makeinstall_std

%files
%{_docdir}/%{name}-*/
%{_bindir}/%{name}*
%{_bindir}/grepmidi
%{_libdir}/%{name}-*/
%{_datadir}/%{name}-*/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}_icon.png
%{_mandir}/man1/grepmidi*
%{_mandir}/man1/%{name}*
%{_datadir}/mime/packages/muse.xml


%changelog
* Tue Jul 31 2012 Frank Kober <emuse@mandriva.org> 2.0.1-1
+ Revision: 811495
- new version 2.0.1

* Fri Jul 13 2012 Frank Kober <emuse@mandriva.org> 2.0-1
+ Revision: 809100
- new (qt4-based) version 2.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Mar 15 2009 Funda Wang <fwang@mandriva.org> 1.0-0.rc1.1mdv2009.1
+ Revision: 355318
- New version 1.0 rc1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9-2mdv2008.1
+ Revision: 170992
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Sep 04 2007 Emmanuel Andry <eandry@mandriva.org> 0.9-1mdv2008.0
+ Revision: 79570
- New version
- drop old menu
- fix URL

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Fri Mar 23 2007 Emmanuel Andry <eandry@mandriva.org> 0.8.1-3mdv2007.1
+ Revision: 148239
- rebuild for libflac

  + Jérôme Soyer <saispo@mandriva.org>
    - Import muse

* Wed Sep 06 2006 Emmanuel Andry <eandry@mandriva.org> 0.8.1-2mdv2007.0
- xdg menu
- %%mkrel

* Wed May 17 2006 Austin Acton <austin@mandriva.org> 0.8.1-1mdk
- fix lib64
- 0.8.1a

* Sat Jan 15 2005 Austin Acton <austin@mandrake.org> 0.7.1-1mdk
- 0.7.1
- fix summary
- configure 2.5
- buildrequires samplerate
- update configure flags
- update description

* Wed Jul 21 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7.0-1mdk
- 0.7.0

* Fri Jul 02 2004 Michael Scherer <misc@mandrake.org> 0.6.3-2mdk 
- rebuild for new gcc ( patch0 )

