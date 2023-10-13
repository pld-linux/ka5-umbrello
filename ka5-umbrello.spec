%define		kdeappsver	23.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		umbrello
Summary:	Umbrello
Name:		ka5-%{kaname}
Version:	23.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	09a1dbe30e9acbde0bc241d4258f7557
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebKit-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	clang-devel >= 2.8.12
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-syntax-highlighting-devel >= %{kframever}
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
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

%package apidocs
Summary:	Apidocs for %{kaname}
Summary(pl.UTF-8):	Dokumentacja API dla %{kaname}
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description apidocs
Apidocs for %{kaname}.

%description apidocs -l pl.UTF-8
Dokumentacja API dla %{kaname}.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications
BuildArch:	noarch

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/po2xmi5
%attr(755,root,root) %{_bindir}/umbrello5
%attr(755,root,root) %{_bindir}/xmi2pot5

%files apidocs
%defattr(644,root,root,755)
%{_datadir}/umbrello5/apidoc

%files data -f %{kaname}.lang
%defattr(644,root,root,755)
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
%exclude %{_datadir}/umbrello5/apidoc
%{_docdir}/qt5-doc/umbrello.qch
