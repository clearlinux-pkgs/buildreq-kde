Name:           buildreq-kde
Version:        1
Release:        43
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

%if 0
Requires:	kauth
Requires:	kauth-dev
Requires:	kconfigwidgets-dev
Requires:	kio-dev
Requires:	kbookmarks-dev
Requires:	kdoctools-dev
Requires:	kdoctools
Requires:	kservice-dev

Requires:	kconfigwidgets-dev
Requires:	kpty-dev
Requires:	kwidgetsaddons-dev
Requires: 	kcodecs-dev
Requires:	knewstuff-dev
Requires:	kcmutils-dev
Requires:	kiconthemes-dev
Requires:	kcompletion-dev
Requires:	kxmlgui-dev
Requires:	kitemviews-dev
Requires:	attica-dev
Requires:	kjobwidgets-dev
Requires:	solid-dev
Requires:	networkmanager-qt-dev
Requires:	NetworkManager-dev
Requires: 	kdelibs4support-dev
Requires:	karchive-dev
Requires:	kcrash-dev
Requires: 	kdbusaddons-dev
Requires: 	kdeclarative-dev
Requires: 	kdesignerplugin-dev
Requires: 	kemoticons-dev
Requires: 	kguiaddons-dev
Requires: 	kinit-dev
Requires: 	kitemmodels-dev
Requires: 	knotifications-dev
Requires: 	kpackage-dev
Requires: 	kparts-dev
Requires: 	ktextwidgets-dev
Requires: 	kunitconversion-dev
Requires: 	kwallet-dev
Requires: 	sonnet-dev
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
