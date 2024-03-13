Name:           buildreq-kde
Version:        1
Release:        66
License:        GPL-2.0
Summary:        Helper files
Url:            https://clearlinux.org/
Group:          base
Requires:       qtbase-dev
Requires:	extra-cmake-modules
Requires:	buildreq-qt6
Requires:	mesa-dev
Requires:	libglvnd-dev
Requires:	pkgconfig(x11)
Requires:	boost-dev
Requires:	lm-sensors-dev

Requires:	qt3d-dev
Requires:	qtcharts-dev
Requires:	qtconnectivity-dev
Requires:	qtdatavis3d-dev
Requires:	qtdeclarative-dev
Requires:	qtgamepad-dev
Requires:	qtgraphicaleffects
Requires:	qtimageformats-dev
Requires:	qtlocation-dev
Requires:	qtmultimedia-dev
Requires:	qtnetworkauth-dev
Requires:	qtquickcontrols2-dev
Requires:	qtremoteobjects-dev
Requires:	qtscript-dev
Requires:	qtscxml-dev
Requires:	qtsensors-dev
Requires:	qtserialbus-dev
Requires:	qtserialport-dev
Requires:	qtspeech-dev
Requires:	qtsvg-dev
Requires:	qttools-dev
Requires:	qttranslations
Requires:	qtvirtualkeyboard-dev
Requires:	qtwayland-dev
Requires:	qtwebchannel-dev
Requires:	qtwebsockets-dev
Requires:	qtxmlpatterns-dev

Requires:	kconfig
Requires:	kconfig-dev
Requires:	kcoreaddons-dev
Requires:	ki18n-dev
Requires:	kwindowsystem-dev
Requires: 	kcodecs-dev
Requires: 	kguiaddons-dev
Requires:	kwidgetsaddons-dev
Requires:	kauth
Requires:	kauth-dev
Requires:	qt6speech-dev
Requires:	kcrash-dev
Requires: 	kdbusaddons-dev
Requires:	solid-dev
Requires:	kiconthemes-dev
Requires:	kconfigwidgets-dev
Requires:	karchive-dev
Requires:	kbookmarks-dev
Requires:	kcompletion-dev
Requires: 	sonnet-dev
Requires:	kitemviews-dev
Requires: 	ktextwidgets-dev
Requires:	kxmlgui-dev
Requires:	kdoctools-dev
Requires:	kdoctools
Requires:	kservice-dev
Requires: 	kwallet-dev
Requires: 	knotifications-dev
Requires:	kio-dev
Requires:	kjobwidgets-dev
Requires: 	kparts-dev
Requires: 	kunitconversion-dev
Requires: 	kitemmodels-dev
Requires: 	kpackage-dev
Requires:	kpty-dev
Requires:	qt5compat-dev
Requires:	kcmutils-dev
Requires:	attica-dev
Requires: 	kdeclarative-dev
Requires:	kirigami2-dev
Requires:	knewstuff-dev
Requires:	kconfigwidgets-dev
Requires:	NetworkManager-dev
Requires:	libkdegames-dev
Requires:	ksvg-dev
Requires:	ktexttemplate-dev
Requires:	libplasma-dev
Requires:	kcolorscheme-dev
Requires:	polkit-qt6-dev
Requires:	plasma5support-dev
Requires:	xdg-desktop-portal-kde

%if 0

Requires: 	kemoticons-dev

Requires:	networkmanager-qt-dev
Requires: 	kdelibs4support-dev
Requires: 	kdesignerplugin-dev
Requires: 	kinit-dev
Requires: 	qtx11extras-dev
#Requires:	kimap-dev
#Requires:	kimap-staticdev
#Requires:	kaccounts-integration-dev
#Requires:	plasma-framework-dev
Requires:        qtkeychain-dev
Requires:	ktextaddons-dev
# compat provides
%endif

Provides: qttools-extras

%description
Helper files

%prep

%build

%install


%files
