%undefine	_debugsource_packages
#define	version_no_zero %%(if [ `echo %%{version}|cut -d. -f3` = 0 ]; then echo -n %%{version} |cut -d. -f1-2; else echo -n %%{version}; fi)
%define		version_no_zero 4.2
%define	major %(echo %{version} |cut -d. -f1)

#%%define _disable_lto 1

Summary:	Midi/Audio Music Sequencer
Name:	muse
Version:	4.2.1
Release:	2
# Original freeverb plugin was public domain; givertcap (not built) is GPLv2
# The rest, including the core of muse is distributed under GPLv2+
License:	Public Domain and GPLv2 and GPLv2+ and LGPLv2+
Group:	Sound
Url:	https://muse-sequencer.github.io/
Source0:	https://github.com/muse-sequencer/muse/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:	muse-4.2.1-use-ladish-in-place-of-lash.patch
Patch1:	muse-4.2.1-fix-python-shebangs.patch
BuildRequires:	cmake >= 3.25
BuildRequires:	desktop-file-utils
BuildRequires:	extra-cmake-modules >= 5.94.0
BuildRequires:git
BuildRequires:	lv2-plugins
BuildRequires:	ninja
BuildRequires:	atomic-devel
BuildRequires:	ladspa-devel
BuildRequires:	python-qt5-devel
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5UiTools)
BuildRequires:	pkgconfig(alsa) >= 1.1.3
BuildRequires:	pkgconfig(dssi) >= 1.1.1
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(jack) >= 1.9.12
BuildRequires:	pkgconfig(libinstpatch-1.0)
BuildRequires:	pkgconfig(liblash)
BuildRequires:	pkgconfig(liblo) >= 0.29
BuildRequires:	pkgconfig(lilv-0)
BuildRequires:	pkgconfig(lrdf) >= 0.5.0
BuildRequires:	pkgconfig(lv2)
#BuildRequires: pkgconfig(lv2-gui)
BuildRequires:	pkgconfig(lv2core)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(Qt5Core) >= 5.9.5
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(raptor2)
BuildRequires:	pkgconfig(rtaudio) >= 5.0
BuildRequires:	pkgconfig(rubberband) >= 1.8.1
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(sord-0)
BuildRequires:	pkgconfig(uuid)
BuildRequires: python-pyro
#Requires:	rtaudio
#Requires:	fluidsynth

%description
MusE is a MIDI/Audio sequencer with recording and editing capabilities. It can
perform audio effects like chorus/flanger in real-time via LADISH and it
supports Jack and ALSA interfaces. MusE aims to be a complete multitrack
virtual studio for Linux.

%files
%{_docdir}/%{name}-*/
%{_bindir}/%{name}*
%{_bindir}/grepmidi
%{_libdir}/%{name}-%{version_no_zero}/
%{_datadir}/%{name}-%{version_no_zero}/
%{_datadir}/applications/io.github.muse_sequencer.Muse.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/grepmidi*
%{_mandir}/man1/%{name}*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/io.github.muse_sequencer.Muse.appdata.xml

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
# MODULES_BUILD_STATIC is needed to workaround linking errors
# Muse needs rpath for finding the libraries, so we cannot use %%cmake
mkdir build
pushd build
cmake .. \
	-DCMAKE_SKIP_RPATH=OFF \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}" \
	-DCMAKE_INSTALL_LIBDIR:PATH="%{_libdir}" \
	-DCMAKE_BUILD_TYPE=Release \
	-DMODULES_BUILD_STATIC=ON \
	-DMusE_DOC_DIR="%{_docdir}/%{name}-%{version}/" \
	-DENABLE_RTAUDIO=ON \
	-DENABLE_FLUID=ON \
	-DENABLE_EXPERIMENTAL=OFF \
	-DENABLE_PYTHON=ON \
	-DENABLE_LASH=ON \
	-DENABLE_RTAUDIO=ON \
	-DENABLE_LV2_GTK2=ON \
	-DENABLE_ZITA_RESAMPLER=OFF \
	-DENABLE_INSTPATCH=ON \
	-G Ninja

%ninja_build


%install
%ninja_install -C build
