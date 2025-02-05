Name:           varia
Version:        2024.5.7
Release:        1%{?autorelease}
Summary:        Download manager based on aria2
License:        MPL-2.0
Group:          System/GUI/GNOME
Url:            https://giantpinkrobots.github.io/varia

Source0:        %{name}-%{version}.tar.gz
BuildArch: noarch

%define typelib() (typelib(%1) = %2 or %{_libdir}/girepository-1.0/%1-%2.typelib)

BuildRequires: (gtk4-tools or gtk4-devel-tools)
BuildRequires: desktop-file-utils
BuildRequires: meson
BuildRequires: fdupes
BuildRequires: filesystem
BuildRequires: gettext
Requires: python3
Requires: python3-gobject
Requires: python3-requests
Requires: python3-aria2p
Requires: %{typelib GLib 2.0}
Requires: %{typelib Gtk 4.0}
Requires: %{typelib Adw 1}
Requires: dconf
Requires: bash
Requires: aria2
Requires: filesystem

%package lang
Summary: Languages for %{name}
%description lang
Language package for %{name}.

%description
Varia is a simple download manager that conforms to the
latest Libadwaita design guidelines, integrating nicely
with GNOME. It uses the amazing aria2 to handle the downloads.

%global __requires_exclude ^/bin/python3$

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}

%files
%doc README.md
%license LICENSE*
%{_bindir}/*
%{_datadir}/glib-2.0/**/*
%{_datadir}/icons/**/*
%{_datadir}/metainfo/*
%{_datadir}/applications/*
%{_datadir}/mime/packages/io.github.giantpinkrobots.varia.mime.xml
%dir %{_datadir}/applications
%dir %{_datadir}/metainfo
%dir %{_datadir}/glib-2.0
%{_datadir}/varia/*
%dir %{_datadir}/varia

%files lang
%{_datadir}/locale/**/*
%dir %{_datadir}/locale

%changelog

