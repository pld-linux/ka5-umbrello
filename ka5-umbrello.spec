%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		umbrello
Summary:	Umbrello
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	13f64d7ea268a16166df994ed7d766a6
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebKit-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-ktexteditor-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Umbrello is a Unified Modelling Language (UML) modelling tool and code
generator. It can create diagrams of software and other systems in the
industry-standard UML format, and can also generate code from UML
diagrams in a variety of programming languages.

Features

- Supported formats: XMI
- Several type of diagrams supported: use case, class, sequence,
  collaboration, state, activity, component, deployment, entity
  relationship

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/po2xmi5
%attr(755,root,root) %{_bindir}/umbrello5
%attr(755,root,root) %{_bindir}/xmi2pot5
%{_desktopdir}/org.kde.umbrello.desktop
%{_iconsdir}/hicolor/128x128/apps/umbrello.png
%{_iconsdir}/hicolor/16x16/apps/umbrello.png
%{_iconsdir}/hicolor/16x16/mimetypes/application-x-uml.png
%{_iconsdir}/hicolor/22x22/apps/umbrello.png
%{_iconsdir}/hicolor/32x32/apps/umbrello.png
%{_iconsdir}/hicolor/32x32/mimetypes/application-x-uml.png
%{_iconsdir}/hicolor/48x48/apps/umbrello.png
%{_iconsdir}/hicolor/64x64/apps/umbrello.png
%{_iconsdir}/hicolor/scalable/apps/umbrello.svgz
%{_datadir}/metainfo/org.kde.umbrello.appdata.xml
%{_datadir}/umbrello5
