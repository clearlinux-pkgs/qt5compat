#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: f4bef72
#
Name     : qt5compat
Version  : 6.6.2
Release  : 7
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qt5compat-everywhere-src-6.6.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qt5compat-everywhere-src-6.6.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt5compat-lib = %{version}-%{release}
Requires: qt5compat-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : icu4c-dev
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt5compat package.
Group: Development
Requires: qt5compat-lib = %{version}-%{release}
Provides: qt5compat-devel = %{version}-%{release}
Requires: qt5compat = %{version}-%{release}

%description dev
dev components for the qt5compat package.


%package lib
Summary: lib components for the qt5compat package.
Group: Libraries
Requires: qt5compat-license = %{version}-%{release}

%description lib
lib components for the qt5compat package.


%package license
Summary: license components for the qt5compat package.
Group: Default

%description license
license components for the qt5compat package.


%prep
%setup -q -n qt5compat-everywhere-src-6.6.2
cd %{_builddir}/qt5compat-everywhere-src-6.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710792152
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710792152
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt5compat
cp %{_builddir}/qt5compat-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt5compat/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qt5compat-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt5compat/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qt5compat-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt5compat/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qt5compat-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt5compat/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qt5compat-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt5compat/f45ee1c765646813b442ca58de72e20a64a7ddba || :
cp %{_builddir}/qt5compat-everywhere-src-%{version}/src/core5/codecs/QBIG5CODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qt5compat/5f1f3a3317504f51b562784738656be8593c7ffa || :
cp %{_builddir}/qt5compat-everywhere-src-%{version}/src/core5/codecs/QBKCODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qt5compat/472d1249930e41755894c5336b785c2753d704a2 || :
cp %{_builddir}/qt5compat-everywhere-src-%{version}/src/core5/codecs/QEUCJPCODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qt5compat/70fabf2a986af11354277144546150a1c9783cac || :
cp %{_builddir}/qt5compat-everywhere-src-%{version}/src/core5/codecs/QEUCKRCODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qt5compat/1118a9b7fdff2e9a736acfe764d3d993715e85bb || :
cp %{_builddir}/qt5compat-everywhere-src-%{version}/src/core5/codecs/QJISCODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qt5compat/70fabf2a986af11354277144546150a1c9783cac || :
cp %{_builddir}/qt5compat-everywhere-src-%{version}/src/core5/codecs/QSJISCODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qt5compat/70fabf2a986af11354277144546150a1c9783cac || :
cp %{_builddir}/qt5compat-everywhere-src-%{version}/src/core5/codecs/QTSCIICODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qt5compat/866627e250d50de077ffe78efa8f585f87238180 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6core5compat_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_core5compat.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_core5compat_private.pri
/usr/lib64/qt6/modules/Core5Compat.json
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/Blend.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/BrightnessContrast.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/ColorOverlay.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/Colorize.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/ConicalGradient.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/Desaturate.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/DirectionalBlur.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/Displace.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/DropShadow.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/FastBlur.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/GammaAdjust.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/GaussianBlur.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/Glow.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/HueSaturation.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/InnerShadow.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/LevelAdjust.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/LinearGradient.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/MaskedBlur.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/OpacityMask.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/RadialBlur.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/RadialGradient.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/RectangularGlow.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/RecursiveBlur.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/ThresholdMask.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/ZoomBlur.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/plugins.qmltypes
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/private/DropShadowBase.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/private/FastGlow.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/private/FastInnerShadow.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/private/GaussianDirectionalBlur.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/private/GaussianGlow.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/private/GaussianInnerShadow.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/private/GaussianMaskedBlur.qml
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/private/plugins.qmltypes
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/private/qmldir
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/qmldir

%files dev
%defattr(-,root,root,-)
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qbinaryjson_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qbinaryjsonarray_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qbinaryjsonobject_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qbinaryjsonvalue_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qcodecmacros_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qicucodec_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qisciicodec_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qlatincodec_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qsimplecodec_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qtcore5compat-config_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qtextcodec_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qtsciicodec_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qutfcodec_p.h
/usr/include/QtCore5Compat/6.6.2/QtCore5Compat/private/qxml_p.h
/usr/include/QtCore5Compat/QBinaryJson
/usr/include/QtCore5Compat/QConcatenable
/usr/include/QtCore5Compat/QLinkedList
/usr/include/QtCore5Compat/QLinkedListData
/usr/include/QtCore5Compat/QLinkedListIterator
/usr/include/QtCore5Compat/QLinkedListNode
/usr/include/QtCore5Compat/QMutableLinkedListIterator
/usr/include/QtCore5Compat/QRegExp
/usr/include/QtCore5Compat/QStringRef
/usr/include/QtCore5Compat/QTextCodec
/usr/include/QtCore5Compat/QTextDecoder
/usr/include/QtCore5Compat/QTextEncoder
/usr/include/QtCore5Compat/QXmlAttributes
/usr/include/QtCore5Compat/QXmlContentHandler
/usr/include/QtCore5Compat/QXmlDTDHandler
/usr/include/QtCore5Compat/QXmlDeclHandler
/usr/include/QtCore5Compat/QXmlDefaultHandler
/usr/include/QtCore5Compat/QXmlEntityResolver
/usr/include/QtCore5Compat/QXmlErrorHandler
/usr/include/QtCore5Compat/QXmlInputSource
/usr/include/QtCore5Compat/QXmlLexicalHandler
/usr/include/QtCore5Compat/QXmlLocator
/usr/include/QtCore5Compat/QXmlNamespaceSupport
/usr/include/QtCore5Compat/QXmlParseException
/usr/include/QtCore5Compat/QXmlReader
/usr/include/QtCore5Compat/QXmlSimpleReader
/usr/include/QtCore5Compat/QtCore5Compat
/usr/include/QtCore5Compat/QtCore5CompatDepends
/usr/include/QtCore5Compat/QtCore5CompatVersion
/usr/include/QtCore5Compat/qbinaryjson.h
/usr/include/QtCore5Compat/qcore5global.h
/usr/include/QtCore5Compat/qlinkedlist.h
/usr/include/QtCore5Compat/qregexp.h
/usr/include/QtCore5Compat/qstringref.h
/usr/include/QtCore5Compat/qtcore5compat-config.h
/usr/include/QtCore5Compat/qtcore5compatversion.h
/usr/include/QtCore5Compat/qtextcodec.h
/usr/include/QtCore5Compat/qxml.h
/usr/lib64/cmake/Qt6/FindWrapIconv.cmake
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/Qt5CompatTestsConfig.cmake
/usr/lib64/cmake/Qt6Core5Compat/Qt6Core5CompatAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Core5Compat/Qt6Core5CompatConfig.cmake
/usr/lib64/cmake/Qt6Core5Compat/Qt6Core5CompatConfigVersion.cmake
/usr/lib64/cmake/Qt6Core5Compat/Qt6Core5CompatConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Core5Compat/Qt6Core5CompatDependencies.cmake
/usr/lib64/cmake/Qt6Core5Compat/Qt6Core5CompatTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Core5Compat/Qt6Core5CompatTargets.cmake
/usr/lib64/cmake/Qt6Core5Compat/Qt6Core5CompatVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectspluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectspluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectspluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectspluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectspluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectspluginTargets.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectsprivateAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectsprivateConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectsprivateConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectsprivateConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectsprivateTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtgraphicaleffectsprivateTargets.cmake
/usr/lib64/libQt6Core5Compat.prl
/usr/lib64/libQt6Core5Compat.so
/usr/lib64/pkgconfig/Qt6Core5Compat.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6Core5Compat.so.6.6.2
/V3/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/libqtgraphicaleffectsplugin.so
/V3/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/private/libqtgraphicaleffectsprivateplugin.so
/usr/lib64/libQt6Core5Compat.so.6
/usr/lib64/libQt6Core5Compat.so.6.6.2
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/libqtgraphicaleffectsplugin.so
/usr/lib64/qt6/qml/Qt5Compat/GraphicalEffects/private/libqtgraphicaleffectsprivateplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt5compat/1118a9b7fdff2e9a736acfe764d3d993715e85bb
/usr/share/package-licenses/qt5compat/472d1249930e41755894c5336b785c2753d704a2
/usr/share/package-licenses/qt5compat/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt5compat/5f1f3a3317504f51b562784738656be8593c7ffa
/usr/share/package-licenses/qt5compat/70fabf2a986af11354277144546150a1c9783cac
/usr/share/package-licenses/qt5compat/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt5compat/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt5compat/866627e250d50de077ffe78efa8f585f87238180
/usr/share/package-licenses/qt5compat/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt5compat/f45ee1c765646813b442ca58de72e20a64a7ddba
