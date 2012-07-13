Name:          muse
Summary:       Midi/Audio Music Sequencer
Version:       2.0
Release:       1
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
%{_docdir}/%{name}-%{version}/
%{_bindir}/%{name}*
%{_bindir}/grepmidi
%{_libdir}/%{name}-%{version}*/
%{_datadir}/%{name}-%{version}*/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}_icon.png
%{_mandir}/man1/grepmidi*
%{_mandir}/man1/%{name}*
%{_datadir}/mime/packages/muse.xml
