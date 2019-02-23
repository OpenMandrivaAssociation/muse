Name:          muse
Summary:       Midi/Audio Music Sequencer
Version:       3.0.2
Release:       1
License:       Public Domain and GPLv2 and GPLv2+ and LGPLv2+
Group:         Sound
URL:           http://www.muse-sequencer.org/
Source0:       https://github.com/muse-sequencer/muse/archive/muse_%(echo %{version} | sed -e 's,\.,_,g').tar.gz
Patch0:		muse-3.0.2-compile.patch
Patch1:		muse-3.0.2-python3.patch

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
BuildRequires: qt5-devel
BuildRequires: desktop-file-utils
BuildRequires: libuuid-devel

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
%{_datadir}/metainfo/muse.appdata.xml
