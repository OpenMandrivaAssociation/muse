#%%define _disable_lto 1
Name:          muse
Summary:       Midi/Audio Music Sequencer
Version:       3.1.0
Release:       1
License:       Public Domain and GPLv2 and GPLv2+ and LGPLv2+
Group:         Sound
URL:           http://www.muse-sequencer.org/
Source0:       https://github.com/muse-sequencer/muse/archive/muse-muse_%(echo %{version} | sed -e 's,\.,_,g').tar.gz
Patch1:	       fix-missing-include.patch
Patch2:	       fix-incomplete-type.patch
Patch3:		muse-3.1.0-experimental-features-fix-build.patch

BuildRequires: libalsa-devel
BuildRequires: jackit-devel
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: dssi-devel
BuildRequires: fluidsynth-devel
BuildRequires: liblo-devel
BuildRequires: libsamplerate-devel
BuildRequires: sndfile-devel
BuildRequires: pkgconfig
BuildRequires: python-devel
BuildRequires: python-qt5
BuildRequires: python-pyro
BuildRequires: qt5-devel
BuildRequires: desktop-file-utils
BuildRequires: libuuid-devel
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: ladspa-devel
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lv2)
BuildRequires: lilv-devel
BuildRequires: sord-devel
BuildRequires: pkgconfig(libinstpatch-1.0)
BuildRequires: pkgconfig(rtaudio)
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(lrdf)
BuildRequires: pkgconfig(lv2core)
BuildRequires: pkgconfig(raptor2)
BuildRequires: pkgconfig(rtaudio)
#BuildRequires: pkgconfig(lv2-gui)
BuildRequires: lv2-plugins
#Requires:  rtaudio
#Requires: fluidsynth
%description
MusE is a MIDI/Audio sequencer with recording and editing capabilities. It can
perform audio effects like chorus/flanger in real-time via LASH and it supports
Jack and ALSA interfaces. MusE aims to be a complete multitrack virtual studio 
for Linux.


%prep
%autosetup -p2 -n muse-muse_%(echo %{version} | sed -e 's,\.,_,g')/muse3

%build
mkdir build
pushd build
cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
	-DCMAKE_BUILD_TYPE=Release \
	-DENABLE_EXPERIMENTAL=ON \
	-DENABLE_PYTHON=ON \
	-DENABLE_LASH=OFF \
	-DENABLE_RTAUDIO=ON \
	-DENABLE_LV2_GTK2=OFF\
	-DENABLE_ZITA_RESAMPLER=OFF \
	-DENABLE_INSTPATCH=ON \
	-G Ninja

#   -DMusE_DOC_DIR=%{_docdir}/%{name}-%{version}/ \
#   -DENABLE_PYTHON=1 -DENABLE_LASH=0 -DENABLE_FLUID=1 \
#   -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR:PATH=%_libdir

%ninja_build

%install
%ninja_install -C build

%files
%{_docdir}/%{name}-*/
%{_bindir}/%{name}*
%{_bindir}/grepmidi
%{_libdir}/%{name}-*/
%{_datadir}/%{name}-*/
%{_datadir}/applications/org.musesequencer.Muse3.desktop
%{_datadir}/icons/hicolor/64x64/apps/org.musesequencer.Muse3.png
%{_mandir}/man1/grepmidi*
%{_mandir}/man1/%{name}*
%{_datadir}/mime/packages/muse.xml
%{_datadir}/metainfo/org.musesequencer.Muse3.appdata.xml
